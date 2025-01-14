'''```
@author jacksonsheep
@note python3 language pracetice
```'''

import sys
import operator
from sys import argv,path


# the single annotation
'''
this is a multi line annotaion
local used in function or class
'''
class basic :
    def printall(message, item):  # print basic data structure
        print (message, end=":")
        print (type(item), end=",")
        print(item)

    def variable():
        print ("\nthe below are variabel test:")
        a = b = c = 1; print (a, b, c)
        a, b, c = 1, 2, 3; print (a, b, c)
        print(c/b)  # float devide
        print(c//b, c%b) # int devide and left a value
        print(c**b)  # c power of b

    def string():
        print ("\nthe below are string test:")
        str = 'hello world!'
        print (str[0:-1]) # except last character
        print (str[2:5]) # index from 2 to 5
        print (str *2)  # twice of str
        print ('bot\tle', r'bot\tle')

    def list_func():
        print ("\nthe below are list test:")
        a = [1, 4]
        b = [2, 3]
        a.extend(b)
        print ("merge two list:", a)
        a.remove(3)
        print ("remove value 3:", a)
        a.append(3)
        print ("add 3 in tail:",a )
        a.pop()
        print ("remove in tail:", a)
        a.reverse()
        print ("reverse list:", a)
        a.sort()
        print ("sort list:", a)
        print ("operator.eq(a,b): ", operator.eq(a,b))
        print ("convert to turbe: ", tuple(a))
        print ("convert to set:", set(a))

    def dict_func():
        print ("\nthe below are dict test:")
        dict = {}; dict['1'] = "tom"; dict['2'] = "jerry"; # init the dictory

        print ("init result:", str(dict))
        dict['2'] = "jake"
        print ("change value:", str(dict))
        print ("convert to list:", dict.items())
        print ("get key list:", dict.keys())
        print ("get value list:", dict.values())

    def tuple_func():
        print ("\nthe below are tuple test:")
        tuple = (1, 2, 3, 4)
        print ("init tuple:", tuple)
        print ("init tuple:", (1,)*4)
        print ("max of tuple", max(tuple))
        print ("min of tuple", min(tuple))
        print ("convert to list:", list(tuple))

    def set_func():
        print ("\nthe below are set test:")
        a = {1, 2, 3, 4}
        b = {9, 8, 1}
        a.add(5)
        print ("add to set:", a) #.update for other container
        a.remove(2)
        print ("remove from set:", a) #.discard for other container
        a.difference(b)
        print ("a - b:", a)
        a.intersection(b)
        print ("ab:", a)
        print ("whether and:", a.isdisjoint(b))
        a.symmetric_difference(b)
        print ("a + b - ab:", a)
        a.union(b)
        print ("a + b:", a)
class user:
    def __new__():
        print('create user object')
        return super()
    def __init__():
        pass

variable()
string()
list_func()
tuple_func()
dict_func()
set_func()
