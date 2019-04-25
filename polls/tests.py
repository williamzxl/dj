from django.test import TestCase

# Create your tests here.

# def fib(n):
#     a, b, count = 0, 1, 0
#     while True:
#         if count > n:
#             return
#         # yield a
#         a, b = b, a+b
#         count += 1


# def outer(func):
#     def inner():
#         print("Login success")
#         result = func()
#         print("log added")
#         return result
#     return inner
#
# @outer
# def f1():
#     print("F1 部门")
# f1()

# def outer(func):
#     def inner(username):
#         print("Login Success!")
#         result = func(username)
#         print("Log success")
#         return result
#     return inner
#
# @outer
# def f1(name):
#     print("%s 正在打印" %name)
#
# f1("jack")
# def print_dire_contents(s_path):
#     import os
#     for s_child in os.listdir(s_path):
#         print(s_child)
#         s_file_path = os.path.join(s_path,s_child)
#         print(s_file_path)
# print_dire_contents(".")
# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
# f(2)
# f(3,[3,2,1])
# f(3)
# print(type(globals()))
# print(globals())
# for k,v in globals().items():
#     print(k,v)
import sys
import time


def bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r = '\r[%s%s]%d%%' % ("="*num, " "*(100-num), rate_num, )
    # print(r)
    sys.stdout.write(r)
    sys.stdout.flush()
#

if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.1)
        bar(i, 100)