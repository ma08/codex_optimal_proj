

def solve(a, b):
    c = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] > b[i] + b[j]:
                c += 1
    return c


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))
