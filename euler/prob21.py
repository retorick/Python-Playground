#!/usr/local/bin/python

class Prob21:
    _factors = []

    def is_prime(self, n):
        _s = int(n**.5)
        _i = 2
        _inc = 1
        while _i <= _s:
            if _n % _i == 0:
                return False
            _i += _inc
        return True


    def factor(self, number_to_factor):
        _f = int(number_to_factor**.5)
        _factors = []

        _tmp_number = number_to_factor
        while _tmp_number % 2 == 0:
            _factors.append(2)
            _tmp_number /= 2

        _possible_prime = 3
        while _possible_prime <= _tmp_number:
            if self.is_prime(_possible_prime) and _tmp_number % _possible_prime == 0:
                _factors.append(_possible_prime)
                _tmp_number /= _possible_prime
            _possible_prime += 2
                
        return _factors
        

    def divisors(self, prime_factors):
        _divlist = [1]
        _items = len(prime_factors)
        for _i in xrange(_items):
            for _j in xrange(1,_items+1):
                _f = reduce(lambda x, y: x*y, [x for x in prime_factors[_i:_i+_j]])
                if not _f in _divlist:
                    _divlist.append(_f)
        _divlist.sort()
        return _divlist


prob = Prob21()
d = prob.divisors([2, 2, 3, 5])
print d
