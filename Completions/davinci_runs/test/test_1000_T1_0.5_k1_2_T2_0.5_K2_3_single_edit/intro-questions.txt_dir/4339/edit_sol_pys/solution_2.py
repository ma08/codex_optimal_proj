

def solve(n, a, b, c):
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] > b[i] + b[j] + c[i] + c[j]:
                c += 1
    return c


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    c = list(map(int, input().split()))[:n]
    print(solve(n, a, b))
