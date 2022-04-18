import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

n = int(input())
a = list(map(int, input().split()))
a.sort()

for i in range(n):
    print(a[i], end=' ')
