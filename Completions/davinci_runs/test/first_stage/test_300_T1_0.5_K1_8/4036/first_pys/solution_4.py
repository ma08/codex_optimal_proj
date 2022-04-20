

from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    if n <= k:
        print("YES")
        print(*[1]*n)
        return

    day = 1
    while n > 2 * (k - day + 1):
        n -= 2 * (k - day + 1)
        day += 1

    if n <= k - day + 1:
        print("YES")
        print(*([2 * (k - day + 1) + 1] * (day - 1) + [n]))
    else:
        print("NO")

main()