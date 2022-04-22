
def solve(a, b):
    return a + b


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(solve(a, b))
