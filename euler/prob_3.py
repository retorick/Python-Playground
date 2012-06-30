#!/usr/local/bin/python

n = 600851475143

def is_prime(n):
    s = int(n**.5)
    i = 2
    inc = 1
    while i <= s:
        if n % i == 0:
            return False
        else:
            pass
        i += inc
    return True

f = int(n**.5)
if f % 2 == 0:
    f += 1

while f >= 3:
    if is_prime(f) and n % f == 0:
        print f
        print n / f
        break
    f -= 2
