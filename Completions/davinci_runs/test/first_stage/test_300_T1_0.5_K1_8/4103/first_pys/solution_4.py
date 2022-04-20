

from sys import stdin
from collections import deque

n, b, a = map(int, stdin.readline().split())
s = list(map(int, stdin.readline().split()))

if a == 0:
    print(b)

elif a == 1:
    a_ = 0
    b_ = 0
    for i in s:
        if i == 1:
            a_ += 1
        else:
            b_ += 1

    if b_ == 0:
        print(a_)
    else:
        print(1 + min(a_, b_))

else:
    z = a + b
    a_ = 0
    b_ = 0
    for i in s:
        if i == 1:
            a_ += 1
        else:
            b_ += 1

    if b_ == 0:
        print(a_)
    else:
        if a_ <= b:
            print(a_ + b_)
        else:
            a_ -= b
            b_ -= a_
            print(a + b_)