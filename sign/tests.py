from django.test import TestCase

# Create your tests here.

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(1,n-i):
            if array[j-1] > array[j]:
                array[j-1],array[j] = array[j], array[j-1]
    return array


def test(a):
    n = len(a)
    for i in range(n):
        for j in range(1,n-i):
            if a[j-1] > a[j]:
                a[j-1],a[j] = a[j],a[j-1]
    return a


def binary_search(list, item):
    low = 0
    hight = len(list) - 1
    while low < hight:
        mid = (low + hight) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            hight = mid - 1
        if guess < item:
            low = mid - 1
    return None

# my_list = [5,3,6,2,10]
# my_list.reverse()
# print(my_list)

def findS(a):
    s = a[0]
    s_i = 0
    for i in range(1,len(a)):
        if a[i] < s:
            s = a[i]
            s_i = i
    return s_i

def s(a):
    new = []
    for i in range(len(a)):
        s = findS(a)
        new.append(a.pop(s))
    return new

# print(s(my_list))
n = [0,9,1,8,1,2,2,3,5,4]

def quicksort(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        less = [i for i in a[1:] if i <= pivot]
        great = [i for i in a[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(great)
# print(quicksort(n))
# i = 0
# while i < len(nums) -1:
#     # print(nums, nums[i], nums[i + 1:])
#     if nums[i] in nums[i + 1:]:
#         n = nums[i]
#         while n in nums:
#             nums.remove(n)
#     else:
#         i += 1
# return nums[0]
#         i = 0
#         while i < len(nums):
#             if nums[i] in nums[i+1:] or nums[i] in nums[0:i]:
#                 print(nums[i], nums[i+1:], nums[0:i+1])
#                 i += 1
#             else:
#                 return nums[i]

t = [2,2,1]
book = dict()
ss = set(t)
print(ss)

# while len(t) != 1:
#     temp = t.pop(0)
#     if temp not in t:
#         print(temp)
#     else:
#         t.remove(temp)
# print(t)
# print(int([1]))
# def rotate(nums, k):
#     # nums = nums[0:-k] +  nums[-k:]
#     # return nums
#     for i in range(k):
#         temp = nums.pop(-1)
#         nums.insert(0, temp)
#     return nums
# h = rotate(t,3)
# print(h)
# from collections import deque
# # import collections
# # a =collections.
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if persion_is_seller(person):
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False

# class Student(object):
#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value, int):
#             raise ValueError('score must be int')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0~100')
#         self._score = value

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


if __name__ == '__main__':
    pass
    # s = Student()
    # s.set_score(60)
    # print(s.get_score())
    # s.score = 1000
    # print(s.score)
    # def person_is_seller(name):
    #     return name[-1] == 'm'
    # graph = {}
    # graph["you"] = ["alice", "bob","claire"]
    # graph["alice"] = ["peggy"]
    # graph["bob"] = ['anuj','peggy']
    # graph["claire"] = ["thom","jonny"]
    # graph["anuj"] = []
    # graph["peggy"] = []
    # graph["thom"] = []
    # graph["jonny"] = []
    # from collections import deque
    # search_deque = deque()
    # search_deque += graph["you"]
    # print(search_deque)
    # searched= []
    # while search_deque:
    #     person = search_deque.popleft()
    #     if person not in searched:
    #         if person_is_seller(person):
    #             print(person + " is a mongo seller")
    #             return True
    #         else:
    #             search_deque += graph[person]
    # return False

    #
    # def line_conf(a,b):
    #     def line(x):
    #         return a*x + b
    #     return line
    # line_A = line_conf(2,1)
    # line_B = line_conf(3,2)
    #
    # print(line_A(1))
    # print(line_B(1))
    from pymysql import cursors, connect
    conn = connect(host='127.0.0.1',
                   user='root',
                   password='222222',
                   db='test',
                   charset='utf8mb4',
                   cursorclass=cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM vendors;'
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)
    finally:
        conn.close()

