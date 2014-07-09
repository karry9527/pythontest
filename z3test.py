__author__ = 'kkk'
from z3 import *

x = Real('x')
y = Real('y')
s = Solver()
s.add(x + y < 5, x > 0, y > 1)
print (s.check())
print (s.model())