#!/usr/local/bin/python

sum = 0
for i in xrange(3,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print sum
