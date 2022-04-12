
def solve(n):
    return "Alice" if n % 2 == 1 else "Bob"  # noqa: E731


if __name__ == "__main__":
    n = int(input())
    print(solve(n))
