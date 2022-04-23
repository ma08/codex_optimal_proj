

def count(n):
    if n % 2 == 0:
        return "YES"
    else:
        return "NO"


def main():
    n = map(int, input().split())
    print(count(n))


if __name__ == '__main__':
    main()
