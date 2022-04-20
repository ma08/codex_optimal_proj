

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    min_a, max_a = min(a), max(a)
    if k == 1:
        print(0)
    elif k == n:
        print(max_a - min_a)
    else:
        count = 0
        for i in range(min_a, max_a):
            if i == min_a:
                count += (a.count(i) - 1)
            else:
                count += a.count(i)
            if count >= k:
                print(i - min_a)
                break

main()

"""
def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    min_a, max_a = min(a), max(a)
    if k == 1:
        print(0)
    elif k == n:
        print(max_a - min_a)
    else:
        count = 0
        for i in range(min_a, max_a):
            if i == min_a:
                count += (a.count(i) - 1)
            else:
                count += a.count(i)
            if count >= k:
                print(i - min_a)
                break

main()
"""