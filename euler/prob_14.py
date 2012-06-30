#!/usr/local/bin/python

class Prob14:
    seq = {}

    def __init__(self, start):
        _maxlen = 0
        _n = 2
        while _n <= start:
            _seq = self.get_seq(_n)
            if len(_seq) > _maxlen:
                _maxlen = len(_seq)
                print "Length: %s" % _maxlen
                print _n, _seq
            _n += 1

    def get_seq(self, n):
        _seq = []
        _orig = n
        while n > 1:
            if n in self.seq:
                _seq.extend(self.seq[n])
                n = 1
            else:
                if n % 2:
                    n = n * 3 + 1
                else:
                    n /= 2
                _seq.append(n) 
        self.seq[_orig] = _seq
        return _seq

prob = Prob14(1000000)
