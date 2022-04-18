
def solve(n, k):
    return "Alice" if k % 2 == 1 else "Bob"


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(solve(n, k))
