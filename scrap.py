# from bs4 import BeautifulSoup
# import requests
#
# # url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
# html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# print(html_text)
# from icecream import ic
# import os
# os.chdir("C:/Users/Eugene/Documents")
# file = open("scrap.txt", "r")
# all = file.readlines()
# any = file.tell()
# few = file.readline()
# for line in all:
#     ic(line)
# ic(all)

# ic(any)
# ic(few)
# file.close()
#Trying to read a closed file will generate an error
# all = file.read()
# ic(all)

# file = open("scrap.txt", "w")
# all = file.write(
#
# )
# ic(all)
# print(all([]))
# print(sum([]))
# import math
# print(math.prod())
# print(len([]))

#Leetcode Challenge

# class Solution(object):
#     def addSum(self, nums, target):
#         # print(nums[1]+nums[2])
#         # print(nums.index(4)) //This will return the index position of the ob
#         for i in nums:
#             for a in nums:
#                 if i+a == target:
#                     print(nums.index(i), nums.index(a))
#
# nums=[2,3,4,7,11]
# target = int(input("Enter a num: "))
#
# result = Solution()
# print(result.addSum(nums, target))


# class caller:
#     def name(self, name1):

#         self.name=name1
#         return name1
# caller_name=caller()
# caller_name2=caller()
# print(caller_name.name('Luke'))
# print(caller_name2.name('Thomas'))

# import re
# import random
# text='sifaoiji ijoijogkejsd ijiojiojav i joijsiogjo ijorgijoas ijeiojrgiojjkgn 45 okdov 48'
# research = re.findall('\d', text)
# print(len(research))
# print(research)
# # print(dir(re))

# string="0244 536 365"
# verify=re.findall('\d*\s+', string)
# print(verify)
# import sys
# import time
# now = time.strftime("%Y-%m-%d %H:%M")
# print(now)
'''ASSERT TEST (This test has limitation when run in an optimized format python -O filename,
 it ignores the test)'''
# def add_positive_nums(x,y):
#     assert x>0 and y>0, "Both expressions must be positive!!!"
#     return x+y

# print(add_positive_nums(2,3))
# print(add_positive_nums(1,-2))

# def junk_food(food):
#     assert food in ["rice", "jollof", "yam", "coffee"], "FOOD must be a JUNK food"
#     return f"NOM NOM NOM {food} is a big JUNK"
# food=input("Please enter a food name: ")
# print(junk_food(food))

# DOCTEST
# Failed test (Run it with python -m doctest -v filename)
# def add_two_numbers(x,y):
#     """
#     >>> add_two_numbers(1,3)
#     4
#     >>> add_two_numbers(100,200)
#     300
#     """
#     return x*y

# Passed test (Run it with python -m doctest -v filename)
# def add_two_numbers(x,y):
#     """
#     >>> add_two_numbers(1,3)
#     4
#     >>> add_two_numbers(100,200)
#     300
#     """
#     return x+y

# def double(value):
#     """Double numbers
#     >>> double([1,2,3,4])
#     [2, 4, 6, 8]
#     >>> double(['a','b','c'])
#     ['aa', 'bb', 'cc']
#     >>> double([])
#     []
#     """
#     return [2*values for values in value]

import math
import unittest
print(math.factorial(4))
print(math.floor(3.14))

# def factorial(x):
#     """factorial of numbers >=0
#     >>> factorial(2)
#     2
#     >>> factorial(4)
#     24
#     >>> factorial(3)
#     6
#     >>> factorial(8)
#     40320
#     """
#     if math.floor(x)!=x:
#         raise ValueError("n must be a positive integer")
#     return math.factorial(x)

# if __name__ == "__main__":
import doctest
doctest.testmod()

print(dir(unittest.TestCase))


    