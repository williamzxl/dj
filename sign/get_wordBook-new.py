import requests
import json

def login_post_with_uname_pwd(uname,pwd,env="test"):
    url = None
    host = None
    if env.lower() == "test":
        url = "https://proxy.langb.cn/accounts/loginByAccount"
        host = "proxy.langb.cn"
    if env.lower() == "shengchan":
        url = "https://proxy.langb.cn/accounts/loginByAccount"
        host = "proxy.langb.cn"
    headers = {
        'channel': "Test",
        'appkey': "WB_8AB3C7DA2F31",
        'appversion': "30102001",
        'content-type': "application/json; charset=utf-8",
        'content-length': "52",
        'host': host,
        'connection': "Keep-Alive",
        'accept-encoding': "gzip",
        'user-agent': "okhttp/3.10.0",
        'cache-control': "no-cache",
    }
    data = {"UserCredential":str(uname),"Password":str(pwd)}
    response = requests.request("POST", url, headers=headers, json=data)
    return json.loads(response.text).get("AccessToken")

def get_all_word_books(host, headers):
    url = "{}/wordBooks/findUserWordBooks".format(host)
    headers.update({'content-length': "0",})
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    json_data = json.loads(answer)
    return json_data.get("UserWordBookList")

def get_WordBook(all_books, WordBookName):
    for book in all_books:
        if WordBookName in list(book.values()):
            UserWordBookID = book.get("UserWordBookID")
            WordBookType = book.get("WordBookType")
            return UserWordBookID, WordBookType

def findAllTask(host, headers, UserWordBookID):
    url = "{}/wordBooks/{}/findTasks".format(host, UserWordBookID)
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    json_data = json.loads(answer)
    currentTask = []
    ct = json_data.get("CurrentTask")
    currentTask.append(str(ct.get("RoutineIdx")))
    all_new_task = []
    for unit in json_data.get("TaskInfos"):
        for task in unit:
            if task.get("R") == 0:
                all_new_task.append(task)
            if task.get("R") != 0:
                task.update({'R': "00"})
                all_new_task.append(task)
    return all_new_task, currentTask

def get_words_info(host, headers, UserWordBookID, index):
    url = "{}/wordBooks/{}/findP1Words?unitIdx={}".format(host, UserWordBookID, index)
    try:
        headers.pop('Content-Length')
    except:
        pass
    response = requests.request("GET", url, headers=headers)
    answer = response.text
    json_data = json.loads(answer)
    return json_data.get("WordInfos")

def post_6_done(host, headers, UserWordBookID, index, RID):
    url = "{}/wordBooks/{}/markTaskItemComplete".format(host, UserWordBookID)
    data = {"UnitIdx":int("{}".format(index)),"RoutineIdx":int("{}".format(int(RID)))}
    headers.update({'Content-Length': '71'})
    response = requests.request("POST", url, headers=headers, json=(data))
    try:
        headers.pop('Content-Length')
    except:
        pass
    return response.status_code

access = login_post_with_uname_pwd("14700000410","111111")
print(access)