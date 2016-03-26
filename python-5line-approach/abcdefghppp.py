#!/usr/bin/python
# -*- coding: utf-8 -*-
# Try to solve this puzzle with python in 5 lines without importing modules

ran = [x for x in range(11, 99) if x % 10 != 0] #no zeros are allowed
#ran = range(10, 99) #no zeros in ACEG are allowed
#ran = range(1, 99) #zero are allowed
l = lambda x, y: x%10!=x/10 and y%10!=y/10 and x%10!=y%10 and x/10!=y/10 and x%10!=y/10 and x/10!=y%10
p = lambda x: x > 100 and x%10==x/10%10==x/10/10
t = lambda x: ([(j,k) for j in ran for k in ran if l(j,k) and l(j,x[0]) and l(j,x[1]) and l(k,x[0]) and l(k,x[1]) and j-k == x[0]], x)
for r in [(y[0], y[1], x[1][1]) for x in list(map(t,[(x,y) for x in ran for y in ran if p(x+y) and l(x,y)])) for y in x[0] if len(x[0]) > 0]: print '%d - %d = %d, %d + %d = %d'%(r[0], r[1], r[0] - r[1], r[0] - r[1], r[2], r[0]-r[1]+r[2])
"""真的用5行solve咗"""
