

def solve(n, a, b, c):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] > b[i] + b[j]:
                count += 1
    return count


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))
