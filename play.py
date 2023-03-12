# import requests
# url = "https://www.github.com"
# import random
# import datetime
# list=[1,2,3,4,5]


# print(dir(random))
# payload = "{\r\n    \"coding\": \"8\",\r\n    \"from\": \"SMSInfo\",\r\n    \"hex-content\": \"00480065006c006c006f\",\r\n    \"to\": 971562316353\r\n}"
# headers = {
#     'content-type': "application/json",
#     'authorization': "undefined",
#     }

# response = requests.request("POST", url)
#
# print(response.text)


# names = ('Alice', 'David', 'Benjamin', 'Tiene')
# rand = random.choice(names)
# my_guess = input("Enter a name: ")
#ic(rand)
# word = 'index'
# high = len(word)
# low = -len(word)
#
# num = random.randrange(low,high)
# ic(num)
# word = input("Enter a word to slice:")
# start = None
# while start !='':
# 	start = input("Start: ")
# 	if start:
# 		start = int(start)
# 		finish = int(input("Enter finish: "))
# 		# ic('word[',start,':', finish,']')
# 		ic(word[start:finish])

#My Version
# from icecream import ic
# word = "mandarin"
# start = int(input("Start: "))
# if start !='':
#     finish = int(input("Finish: "))
#     ic(word[start:finish])
# import os
# os.chdir("C:/Users/Eugene/Documents")
# file = open('play.txt', "w")
# a = ("Welcome to my garden")
# b= ("This is the wall that I built")
# c = ("To protect the people I love")
# write = file.write("{} {} {}\n".format(a,b,c))
# ic(write)
# x=int(input("Enter a number: \n"))
#
# result=(lambda x: x**2)
# print(result(x))

# def tester(start):
#     state=start
#     def nested(label):
#         print(label, state)
#     return nested
# F=tester(0)
# F('spam')

# def tester(start):
#     state=start
#     def nested(label):
#         nonlocal state
#         print(state, label)
#         state+=1
#     return nested
# F=tester(50)
# F('spam')
# F('pam')
# F('am')
# F('m')

# class Tester:
#     def __init__(self, start):
#         self.state=start
#     def nested(self, label):
#         print(label, self.state)
#         self.state+=1
        
# F=Tester(0)
# F.nested('sam')
# F.nested('sam')
# F.nested('sam')

# G=Tester(50)
# for i in range(5):
#     G.nested('spam')

# class Tester:
#     def __init__(self, start):
#         self.state=start
#     def __call__(self, label): #with operator overloading, you can call the function without any method
#         print(label, self.state)
#         self.state+=1
        
# F=Tester(0)
# F('pam')

# def tester(start):
#     def nested(label):
#         print(label, nested.state)
#         nested.state+=1
#     nested.state=start
#     return nested
# F=tester(0)
# F('spam')

# from multiprocessing.pool import ApplyResult


# def state(x, y):
#     x=1
#     y=[2,3]
#     return x,y
# X=2
# Y=[1,2]
# X,Y=state(X,Y)
# X,Y

# def f(*T):
#     return T
# print(f(10))

# def kw(a, b, c):
#     print(a,b,c)
# G={"a":1,"b":2,"c":3}

# print((kw(**G)))

def add(sub, a,b):
    print("calling")
    return a+b
def sub(a,b):
    return a*b
print(add(sub, 5,6))



