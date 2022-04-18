#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for

n = int(input())

for i in range(1, n + 1):
    print(i)

# while

n = int(input())

i = 1
while i <= n:
    print(i)
    i += 1

# if

a, b = map(int, input().split())

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
else:
    print('a == b')

# input

a, b = map(int, input().split())

# output

print(a + b)

# list

l = [1, 2, 3, 4, 5]
l.append(6)
print(l)
print(l.pop())
print(l)
print(l[0])
print(l[-1])
print(l[1:3])

# dict

d = {'foo': 1, 'bar': 2}
print(d['foo'])
print(d.get('baz', 0))

# sample

n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = [0] * n
for i in range(1, n):
    ans[i] = min(ans[i - 1] + a[i - 1], ans[i - 1] + c + b[i - 1])

print(*ans)
