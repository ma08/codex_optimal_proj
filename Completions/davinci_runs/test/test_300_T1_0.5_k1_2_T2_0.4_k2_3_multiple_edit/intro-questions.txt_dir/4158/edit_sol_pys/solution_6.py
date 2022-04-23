


# https://codeforces.com/problemset/problem/1146/A
# Wrong Answer
# 1/6

n = int(input())
s = input()
a = s.count('a')
b = s.count('b')

if a > b:
    print(s.replace('a', '', a - b))
elif a < b:
    print(s.replace('b', '', b - a))
else:
    print(s)
