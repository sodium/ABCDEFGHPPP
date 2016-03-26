#!/usr/bin/python
# -*- coding: utf-8 -*-
# Try to solve this puzzle with python in 5 lines without importing modules

ran = [x for x in range(11, 99) if x % 10 != 0] #no zeros are allowed
#ran = range(10, 99) #no zeros in ACEG are allowed
#ran = range(1, 99) #zero are allowed
no_repeat = lambda x, y, p: x%10!=x/10 and y%10!=y/10 and x%10!=y%10 and x/10!=y/10 and x%10!=y/10 and x/10!=y%10 and x%10!=p and x/10!=p and y%10!=p and y/10!=p
ppp = lambda x: x > 100 and x%10==x/10%10==x/10/10
abcdgh = lambda x: ([(j,k) for j in ran for k in ran if no_repeat(j,k, sum(x)%10) and no_repeat(j,x[0], sum(x)%10) and no_repeat(j,x[1], sum(x)%10) and no_repeat(k,x[0], sum(x)%10) and no_repeat(k,x[1],sum(x)%10) and j-k == x[0]], x)
for r in [(y[0], y[1], x[1][1]) for x in list(map(abcdgh,[(x,y) for x in ran for y in ran if ppp(x+y) and no_repeat(x,y,(x+y)%10)])) for y in x[0] if len(x[0]) > 0]: print '%d - %d = %d, %d + %d = %d'%(r[0], r[1], r[0] - r[1], r[0] - r[1], r[2], r[0]-r[1]+r[2])
"""真的用5行solve咗"""
