#!/usr/local/bin/python

p = [2]
def is_prime(n):
    _max = int(n**.5)
    for _i in p:
        if _i > _max:
            break

        if n % _i == 0:
            return False
    
    p.append(n)
    return True

def sum_primes_less_than(n):
    _total = 2
    _i = 3
    while _i < n:
        if is_prime(_i):
            print _i
            _total += _i
        _i += 2
    return _total

print sum_primes_less_than(2000000)
