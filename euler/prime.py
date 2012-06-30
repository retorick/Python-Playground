#!/usr/local/bin/python

p = []
def is_prime(n):
    _max = int(n**.5)
    for _i in p:
        if _i > _max:
            break

        if n % _i == 0:
            return False
    
    p.append(n)
    return True

def find_nth_prime(n):
    _primes = 0
    _i = 2
    while _primes < n:
        if is_prime(_i):
            _primes += 1
        _i += 1
    return max(p)

print find_nth_prime(10001)
