#!/bin/python3
integer = 1
double = 10.80
_float = 0.10
string = 'hello'
string1 = "hello"


print(string[1])    # e
print(string[0])    # h
print(string[0:4])  # hell
print(string[1:5])  # ello
print(string[:3])   # hel


list = [1234,0.54,5.43,'435',"lol"]         # [1234, 0.54, 5.43, '435', 'lol']
list2 = [ 1234, 0.54, 5.43, '435', "lol"]    # use spaces to make code easier to read
print(list)
print(list2)                                 
print(list[1])                              # 0.54
print(list[1:3])                            # 0.54, 5.43
print(list * 2)                             # [1234, 0.54, 5.43, '435', 'lol', 1234, 0.54, 5.43, '435', 'lol']
print(list + list2)                         # [1234, 0.54, 5.43, '435', 'lol', 1234, 0.54, 5.43, '435', 'lol']
list[1] = 'new value'                       # [1234, 'new value', 5.43, '435', 'lol']
print(list)                                 # 
# print(list)                                 #
# print(list)                                 #
# print(list)                                 #
# print(list)                                 #
# print(list)                                 #


"""
lists in python are mutable
"""

