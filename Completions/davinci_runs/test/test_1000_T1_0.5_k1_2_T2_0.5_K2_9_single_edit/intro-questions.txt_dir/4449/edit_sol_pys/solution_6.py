

from collections import defaultdict

def main():
    n, m = map(int, input().strip().split(' '))
    a, b = [], []
    for i in range(n):
        a.append(input().strip())
    for i in range(m):
        b.append(input().strip())
    print(solve(n, m, a, b))

def solve(n, m, a, b):
    result = 0
    for i in range(n):
        for j in range(m):
            if a[i] == b[j]:
                result += 1
    return result

if __name__ == "__main__":
    main()
