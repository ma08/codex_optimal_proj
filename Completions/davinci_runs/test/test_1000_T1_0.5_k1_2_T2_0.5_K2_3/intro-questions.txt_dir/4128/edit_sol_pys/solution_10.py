

def solve(n, a, b):
    return n // 2 if n % 2 == 0 else n // 2 + 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, a, b = [int(x) for x in input().split()]
        print(solve(n, a, b))
