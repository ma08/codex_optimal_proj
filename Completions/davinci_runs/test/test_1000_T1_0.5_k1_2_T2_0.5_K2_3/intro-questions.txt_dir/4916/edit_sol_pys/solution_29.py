
import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input().split())
print(a)
