
def solve(a: int, b: int) -> int:
    """Compute A * B."""
    return a * b


def main() -> None:
    """Main function."""
    a, b = map(int, input().split())
    print(solve(a, b))


if __name__ == '__main__':
    main()
