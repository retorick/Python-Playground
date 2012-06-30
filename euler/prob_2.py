#!/usr/local/bin/python

result = 0
fib1 = 1
fib2 = 2
while fib2 <= 4000000:
    if fib2 % 2 == 0:
        result += fib2
    fib1, fib2 = fib2, fib1+fib2
print result
