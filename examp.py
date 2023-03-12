# from email.policy import strict


# list_of_names=['Marcus', 'Gina', 'Edward', 'Armando']

# print(dir(list_of_names))
# list_of_names.sort()
# print(" #".join(list_of_names))

# names=['Marcus', 'Gina', 'Edward', 'Armando']
# nums=[4,5,7,8]
# sort_nums=(nums.__add__([2,1,3]))

# print(nums)

# names_nums=dict(zip(names, nums))
# print(names_nums)
# print(names_nums['Edward'])

# magic_num=int(input("Enter a num: "))
# while True:
#     # magic_num=input("Enter a num: ")
#     if magic_num<20:
#         magic_num=int(input("Enter a num: "))
#     else:
#         print("Magic number finally greater than 20")
#         break
# x=[]
# print(dir(x))
# print(type(x))
# x.append(1)
# x.append(3)
# x.append(5)
# x.append(7)
# x.append(9)
# i=0
# while i<len(x):
#     if x[i]>=5:
#         x[i]=x[i]**2
#     i+=1
# print(x)

# y=[2,4,5,6,2]
# for i in y:
#     print(i.__sizeof__())

# num_comp=[i*2 for i in y if i%2==0]
# print(num_comp)

# names_lower=['duvan', 'thomas', 'cyril', 'aldirdge']
# # print(names_lower[0].upper())
# names_comp=[name[0].upper() for name in names_lower]
# print(names_comp)
# print(names_lower)

# from __future__ import nested_scopes
# from tkinter import Y


# num_comp=int(input('Enter a number: '))
# while True:
#     num_comp=int(input('Enter a number: '))
#     if num_comp<20:
#         num_range=[num*2 for num in range(num_comp) if num%2==0]
#         print(num_range)
#     else:
#         print("YOU FAILED")
#         print("TRY again")
#         break
        
# nested_list=[['neal', 'gravan',8], [4,5,6], ['toyota', 'nissan', 'lexus']]
# for list in nested_list:
#     print(list[2])

# DICTIONARIES
# d={'name':'Eugene', 'age':15, 'gender':'male'}
# print(d.pop('age'))
# print(d['name'])
# print(dir(d))

# playlist={
#     'album':'Anloga Junction',
#     'author':'Stonebwoy',
#     'songs':[{'title':'sobolo', 'artist':'stonebwoy x BHIM band', 'duration':5},
#         {'title':'everlasting', 'artist':'stonebwoy', 'duration':3},
#         {'title':'norminate', 'artist':'stonebwoy x Keri hilson', 'duration':3.25}
#     ]
# }
# for artists in playlist['songs']:
#     print(artists['artist'])
#     print('--------------------------------')
# total=0
# for song in playlist['songs']:
#     total +=song['duration']
    
#     print(song.keys())
#     print(song['duration'])
# print(total)

# instructor={'name':'eugene', 'city':'ashaiman', 'favorite_color':'blue'}
# instructor1={k:v.upper() for k,v in instructor.items()}
# print(instructor1)
# print(instructor1['favorite_color'])
# num_set1={1,2,4,5,8,4,3,2,1, 10, 12, 15}

# print({(x/2) for x in num_set | num_set1}, 'union')
# print((num_set))
# num_set=(1,2,4)
# for i in num_set:
#     if True:
#         def even():
#             if i%2==0:
#                 print("Great")
#             else:
#                 print("Cool")
# num_even=even()
# print(num_even)

# def intersect(x1,x2):
#     return [x for x in x1 if x in x2]
# x1="SPAM"
# x2="SCAM"
# res=intersect(x1,x2)
# print(res)

# import examp2
# def caller(x=10):
#     return examp2.hider()+ 15 + examp2.add(2,5)
# print(caller())

# print(examp2.test())

# X = 99 # Global scope name: not used
# def f1():
#     X = 88 # Enclosing def local
#     def f2():
#         print(X) # Reference made in nested def
#     f2()
# f1()

#print(examp2.add_another_func()) #return (add_another_func()) function from examp2.py

# f=examp2.num1(2)
# print(f(3))
# def captain(*arg,**kwargs):
#     kwargs['madrid']='Spain'
#     kwargs['madrid2']='Barcelona'
#     kwargs['madrid3']='Spain'
#     kwargs['madrid4']='Spain'
#     arg=[1,2,5]
#     print(kwargs['madrid2'])
#     for keys,values in kwargs.items():
#         print((values))
#     return kwargs
# print(captain())

# from random import random
# def flip_coin():
#     if random()>0.5:
#         return "Pass"
#     else:
#         return 'Fail'
# print(flip_coin())

# def square(num, pow):
#     return num**pow
# print(square(num=2, pow=3))
# print(square(pow=4, num=2))




# INTERVIEW

seta={1,2,4,5,6,3}
setb={1,2,8,9,10}
print(seta|setb)
