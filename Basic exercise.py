# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

testArr = [11, 22, 33, 22, 11] 
result = testArr[0] 
for iter in testArr: 
 if iter > result: 
  result = iter
print(result)

'''-----------------------------------------'''

import random
print(random.seed(3))


'''-----------------------------------------'''

mylist=['a', 'aa', 'aaa', 'b', 'bb', 'bbb']
print(mylist[:-1])
print(mylist[int(-1/2)])
print(int(-1/2))

'''-----------------------------------------'''

mylist=['abc','cde','abcde','efg', 'ah']
print(max(mylist))

'''-----------------------------------------'''

mylist=[1, 5, 9, int('0')]
print(sum(mylist))

'''-----------------------------------------'''

var1 = True
var2 = False
var3 = False
if var1 or var2 and var3:
 print("True")
else:
 print("False")


'''-----------------------------------------'''

def test():
 try:
  return 1
 finally:
  return 2
result = test()
print(result)

'''-----------------------------------------'''

import random
mylist = [10, 20, 30]
random.shuffle(mylist)
print(mylist)

'''-----------------------------------------'''
print(type(1J))

print(3/5)

'''-----------------------------------------'''

def f():
	pass
print(type(f()))

'''-----------------------------------------'''

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[4::-2])
print(max(a[2:4] + ['grault']))

'''-----------------------------------------'''

print('a' + 'x' if '123'.isdigit() else 'y' + 'b')

'''-----------------------------------------'''

x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1:])

'''-----------------------------------------'''

a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]
print(a)
print(b)
print(c)

'''-----------------------------------------'''

x = 5
y = -5
x, y = (y, x)[::-1]
print(x)
print(y)


'''-----------------------------------------'''

b = 'Hello world I\'m robot'
c = 'robot are not good for the world'

setB = set(list(b.replace(" ", "")))
setC = set(list(c.replace(" ", "")))

val = setB & setC
print(val)

'''-----------------------------------------'''

def find_sum(a,b):
    try:
        print(a+c)
    except ValueError:
        print("Function name error")
    finally:
        print("Sum finally")
try:
    find_sum(12,13)
except NameError:
    print("Invocation name error")
finally:
    print("Invocation finally")