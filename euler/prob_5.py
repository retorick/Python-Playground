#!/usr/local/bin/python

def sq(n):
    return n**2

sum_sq = sum(map(sq, range(101)))

sq_sum = sum(range(101))**2

print sum_sq, sq_sum, sq_sum-sum_sq
