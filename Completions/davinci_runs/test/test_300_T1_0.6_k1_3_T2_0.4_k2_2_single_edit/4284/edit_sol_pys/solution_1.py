
import sys

sys.stdin = open('input.txt')

def play(k, n, a, b):
    if k < a or k < b:
        return -1
    if k < a + b:
        return 1
    return (k - a) // b + 1

q = int(input())
for _ in range(q):
    k,n,a,b = map(int,input().split())
    print(min(play(k,n,a,b),n))
