
import math

def main():
    n = int(input())
    p = list(map(int, input().split()))
    v = list(map(int, input().split()))
    d = [0] * n
    for i in range(n):
        d[i] = p[i]
    for i in range(n):
        for j in range(i + 1, n):
            if d[j] < d[i] and v[j] > v[i]:
                d[j] = d[i] + p[j]
            elif d[i] < d[j] and v[i] > v[j]:
                d[i] = d[j] + p[i]
    print(max(d))


if __name__ == "__main__":
    main()
