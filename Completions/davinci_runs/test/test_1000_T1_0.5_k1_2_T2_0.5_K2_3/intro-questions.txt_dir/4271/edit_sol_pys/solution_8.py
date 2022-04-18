
# https://www.codechef.com/problems/COW1

from sys import stdin, stdout

n, k = [int(a) for a in stdin.readline().split()]
cows = [int(a) for a in stdin.readline().split()]

cows.sort()

result = 0
if cows[0] > 0:
    result = cows[0]

i = 0
while i < n - 1:
    if cows[i + 1] - cows[i] > 1:
        result += cows[i + 1] - cows[i] - 1
    i += 1

if cows[n - 1] < k:
    result += k - cows[n - 1]

print(result)
