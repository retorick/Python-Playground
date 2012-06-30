#!/usr/local/bin/python

n1 = 999
n2 = 999
palin = []
for n1 in range(800,1000)[::-1]:
    for n2 in range(800,1000)[::-1]:
        prod = str(n1 * n2)
        if prod == prod[::-1]:
            palin.append(prod)
print palin

