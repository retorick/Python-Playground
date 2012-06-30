#!/usr/local/bin/python

print sum([x for x in xrange(3,1000) if x % 3 == 0 or x % 5 == 0])
