
def f(n: int) -> int:
    n = n + 1
    while n % 10 == 0:
        n = n // 10
    return n


def main() -> None:
    n = int(input())
    memo = set()
    while n not in memo:
        memo.add(n)
        n = f(n)
    print(len(memo))

if __name__ == "__main__":
    main()
