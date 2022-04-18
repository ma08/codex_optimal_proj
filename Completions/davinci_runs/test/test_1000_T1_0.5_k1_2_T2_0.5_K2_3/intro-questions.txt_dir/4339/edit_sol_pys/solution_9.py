

def solve(n, a, b):
    c = [0] * n
    for i in range(n):
        c[i] = a[i] + b[i]
    c.sort()
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if c[i] < c[j]:
                count += 1
    return count


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))
