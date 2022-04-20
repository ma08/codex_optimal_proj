

# Solution
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

first_team = [0]*n
second_team = [0]*n

a_sorted = sorted(a)

for i in range(n):
    index = a.index(a_sorted[i])
    if index-k >= 0:
        left = index-k
    else:
        left = 0
    if index+k <= n-1:
        right = index+k
    else:
        right = n-1
    if i%2 == 0:
        first_team[left:right+1] = [1]*(right-left+1)
    else:
        second_team[left:right+1] = [1]*(right-left+1)
    a = a[:left] + a[right+1:]

for i in range(n):
    if first_team[i] == 1:
        print(1, end='')
    else:
        print(2, end='')
print()