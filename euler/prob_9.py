#!/usr/local/bin/python

clist = []
alist = []
def is_pythag(a2, b2, c2):
    _a2, _b2 = int(a2**.5)**2, int(b2**.5)**2
    if _a2 + _b2 == c2:
        return True
    else:
        return False
    


def pythag(c):
    _blist = map(lambda x: c % x == 0, clist)
    _result_c = []
    if _blist:
        _result_a = [alist[x] for x in xrange(0,len(_blist)) if _blist[x]]
        _result_c = [clist[x] for x in xrange(0,len(_blist)) if _blist[x]]

    if _result_c:
        _a = _result_a[0]
        _c = _result_c[0]
        _b2 = _c**2 - _a**2
        _b = int(_b2**.5)
        _p = [_a*c/_c, _b*c/_c,c, _a, _b, _c]
    else:
        _c2 = c**2
        _a2 = int(_c2 / 2)
        while _a2 > 3 and is_pythag(_a2, _c2 - _a2, _c2) == False:
            _a2 -= 1
        if _a2 == 3:
            _p = []
        else:
            _a = int(_a2**.5)
            _p = [_a, int((_c2-_a2)**.5), c]
            clist.append(c)
            alist.append(_a)

    return _p

for i in xrange(330,800):
    _p = pythag(i)
    if _p:
        _s = sum(_p[0:3])
        print _p, _s
        if _s==1000:
            print 'Bingo!'

