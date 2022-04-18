import sys


f = open('test.txt')
sys.stdin = f

n = int(f.readline())
a = list(map(int, f.readline().split()))

print(n)
print(a)
