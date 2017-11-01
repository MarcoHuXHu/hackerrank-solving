#!/bin/python3

import sys

d = 5
digit = 10 ** d

def multiple(a, x):
    for i in range(len(a)):
        a[i] = a[i] * x
    for i in range(len(a)):
        k = a[i] // digit
        a[i] = a[i] % digit
        if k > 0:
            if i == len(a) -1:
                a.append(k)
            else:
                a[i + 1] = a[i + 1] + k
    return(a)

n = int(input().strip())
a = [1]
for i in range(1, n + 1):
    a = multiple(a, i)
a = list(map(str, a))
b = a[-1:]
for i in range(len(a) - 2, -1 ,-1):
    b.append('0' * (d - len(a[i])) + a[i])
print(''.join(b))
