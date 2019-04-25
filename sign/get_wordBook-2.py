import requests
import json


class GetAccessToken(object):
    def __init__(self,env='test'):
        self.host = None
        if env.lower() == 'test':
            self.proxy_host = "https://proxy.langb.cn"
        if env.lower() == 'prep':
            self.proxy_host = "https://prep-proxy.langlib.com"
        if env.lower() == 'shengchan':
            self.proxy_host = "https://proxy.langlib.com"
        self.headers = {
            'channel': "Test",
            'appkey': "WB_8AB3C7DA2F31",
            'appversion': "30102001",
            'content-type': "application/json; charset=utf-8",
            'content-length': "52",
            'host': None,
            'connection': "Keep-Alive",
            'accept-encoding': "gzip",
            'user-agent': "okhttp/3.10.0",
            'cache-control': "no-cache",
        }

    def login_post_with_uname_pwd(self,uname, pwd):
        self.url = "{}/accounts/loginByAccount".format(self.proxy_host)
        self.host = self.proxy_host
        data = {"UserCredential": str(uname), "Password": str(pwd)}
        self.headers.update({'host':self.host.split('//')[1]})
        print(self.url)
        response = requests.request("POST", self.url, headers=self.headers, json=data)
        print(json.loads(response.text).get("AccessToken"))
        return json.loads(response.text).get("AccessToken")


class WordBooks(object):
    def __init__(self, accesstoken,env='test'):
        self.host = None
        self.test_host = "https://appwb.langb.cn"
        self.prep_host = "https://prep-appwb.langlib.com"
        self.shengchan_host = "https://appwb.langlib.com"
        self.headers = {
            'channel': "Test",
            'accesstoken':accesstoken,
            'appkey': "WB_8AB3C7DA2F31",
            'appversion': "30102001",
            'host': None,
            'connection': "Keep-Alive",
            'accept-encoding': "gzip",
            'user-agent': "okhttp/3.10.0",
            'cache-control': "no-cache",
        }
        self.env = env
        if self.env == 'test':
            self.host = self.test_host.split("//")[1]
        if self.env == 'prep':
            self.host = self.prep_host.split("//")[1]
        if self.env == 'shengchan':
            self.host = self.shengchan_host.split("//")[1]
        print(self.host)

    def get_all_word_books(self):
        if self.env == 'test':
            self.url = "{}/wordBooks/findUserWordBooks".format(self.test_host)
        if self.env == 'prep':
            self.url = "{}/wordBooks/findUserWordBooks".format(self.prep_host)
        if self.env == 'shengchan':
            self.url = "{}/wordBooks/findUserWordBooks".format(self.shengchan_host)
        self.headers.update({'content-length': "0", })
        response = requests.request("GET", self.url, headers=self.headers)
        answer = response.text
        json_data = json.loads(answer)
        return json_data.get("UserWordBookList")

    def get_WordBook(self,all_books, WordBookName):
        for book in all_books:
            if WordBookName in list(book.values()):
                UserWordBookID = book.get("UserWordBookID")
                WordBookType = book.get("WordBookType")
                return UserWordBookID, WordBookType

    def findAllTasks(self, UserWordBookID):
        url = "https://{}/wordBooks/{}/findTasks".format(self.host, UserWordBookID)
        response = requests.request("GET", url, headers=self.headers)
        answer = response.text
        tasks_data = json.loads(answer)
        return tasks_data

    def get_words_info(self,UserWordBookID, index):
        url = "https://{}/wordBooks/{}/findP1Words?unitIdx={}".format(self.host, UserWordBookID, index)
        try:
            self.headers.pop('Content-Length')
        except:
            pass
        response = requests.request("GET", url, headers=self.headers)
        answer = response.text
        json_data = json.loads(answer)
        return json_data.get("WordInfos")

    def put_words_to_3_star(self,UserWordBookID, id):
        url = "https://{}/wordBooks/{}/updateFamiliarity".format(self.host, UserWordBookID)
        data = {"SysWordID": "{}".format(id), "Phase": 2, "OldFamiliarity": 1, "NewFamiliarity": 2}
        response = requests.request("PUT", url, headers=self.headers, json=data)


    def post_6_done(self,UserWordBookID, index, RID):
        url = "https://{}/wordBooks/{}/markTaskItemComplete".format(self.host, UserWordBookID)
        data = {"UnitIdx": int("{}".format(index)), "RoutineIdx": int("{}".format(int(RID)))}
        self.headers.update({'Content-Length': '71'})
        response = requests.request("POST", url, headers=self.headers, json=(data))
        try:
            self.headers.pop('Content-Length')
        except:
            pass
        return response.status_code


if __name__ == '__main__':
    accesstoken = GetAccessToken(env='shengchan') #指定环境，测试：test;预发：prep,生产：shengchan
    ac = accesstoken.login_post_with_uname_pwd(15600123315,"111111") #用户名及密码
    wb = WordBooks(ac,env='shengchan')#指定环境，测试：test;预发：prep,生产：shengchan
    all_books = wb.get_all_word_books()
    UserWordBookID, WordBookType = wb.get_WordBook(all_books, "托福词汇") #词汇书名称
    # GRE 互联网+，四级高频 2000 词，高考 3500 词
    for i in range(600):
        all_new_task = wb.findAllTasks(UserWordBookID)
        UnitIdx = all_new_task.get('CurrentTask').get('UnitIdx')
        RoutineIdx = all_new_task.get('CurrentTask').get('RoutineIdx')
        wb.post_6_done(UserWordBookID,UnitIdx,RoutineIdx)
