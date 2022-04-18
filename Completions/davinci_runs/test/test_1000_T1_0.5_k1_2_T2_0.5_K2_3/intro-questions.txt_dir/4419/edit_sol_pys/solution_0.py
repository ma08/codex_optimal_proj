# Problem : https://www.acmicpc.net/problem/2839

# SOLUTION
import sys

# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
if n % 5 == 0:
    print(n // 5)
else:
    for i in range(n // 5, -1, -1):
        if (n - 5 * i) % 3 == 0:
            print(i + (n - 5 * i) // 3)
            break
    else:
        print(-1)
