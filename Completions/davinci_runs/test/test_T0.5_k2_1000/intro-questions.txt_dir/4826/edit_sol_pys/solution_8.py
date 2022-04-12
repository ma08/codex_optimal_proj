
def solve(n):
    return "Alice" if n % 2 == 0 else "Bob"


if __name__ == "__main__":
    n = int(input())
    print(solve(n))
