


def is_multiple_of_nine(n: str) -> bool:
    if len(n) == 1:
        return int(n) % 9 == 0
    return is_multiple_of_nine(str(sum(map(int, n))))


if __name__ == "__main__":
    n = input()
    print("Yes" if is_multiple_of_nine(n) else "No")