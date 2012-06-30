#!/usr/local/bin/python

def is_pythag(a, b, c):
    _a2, _b2, _c2 = a**2, b**2, c**2
    if _a2 + _b2 == _c2:
        return True
    else:
        return False


def sum_loop(m):
    _m = int(m*2/3)
    for _a in xrange(3,_m):
        for _b in xrange(_a+1,_m):
            if _a + _b <= m*2/3:
                _c = m - (_a + _b)
                if is_pythag(_a, _b, _c):
                    return [_a, _b, _c]
            
triplet = sum_loop(1000)
prod = reduce(lambda x, y: x*y, triplet)
print triplet, sum(triplet), prod
