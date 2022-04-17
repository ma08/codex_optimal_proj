'''
Author: Rishika Haritha - 20186041
Encoding: Utf-8
'''

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n < k:
        print(1)
    else:
        print(n // k + n % k)
