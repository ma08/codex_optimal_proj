from collections import defaultdict

n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    print(*solve(n, a))
