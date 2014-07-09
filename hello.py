#__author__ = 'kkk'

import random
o = object()
print("Hello World!")
print(o)


print(0.2.as_integer_ratio())

print(0.235.is_integer())

print(2.000.is_integer())

class Demo:
    def setAtt(self, a = 22, b = 33):
        self.a = a
        self.b = b

    def do_something(self):
        return self.a + self.b

print
d = Demo()
d.setAtt(333, 444)
print(d.do_something())
d.setAtt(11, 22)
print(d.do_something())
print

b = {1:0, "4":"XD"}
for i in range(1, 5):
    b[i] = i
#print (b["4"])
print b

balance = 50
if balance >= 10000:
    print 1
elif 10000 > balance >= 100:
    print 2
else:
    print 3


class test:
    def __init__(self, data):
        self.data = data


l = [1, 2, 3, 4]
t = test(l)
import copy
a = copy.copy(t)
b = copy.deepcopy(t)
l.append(5)
print a.data
print b.data

sl = {"s":1, "c1":2}
var = ["s", "p", "c1", "c2"]
for v in var:
    if not v in sl.keys():
        sl[v] = 0
        print ("v", v, "slk", sl.keys())
        print("sl", sl, "var", var)

v = "s"
if not v == "s" or v == "p":
    print "sss"
v = "p"
if not v == "s" or v == "p":
    print "ppp"

