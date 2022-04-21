
import itertools
import sys

sys.setrecursionlimit(2 * 10 ** 5)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

ans = 0
for a, b, c in itertools.combinations(arr, 3):
    if a + b > c and a + c > b and b + c > a and a + b + c > k:
        ans += 1

print(ans)
print(ans1 + 1, ans2 + 1, ans3 + 1)
