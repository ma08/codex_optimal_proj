

def solve(x):
    year = 0
    balance = 100
    while balance < x:
        balance += balance // 100
        year += 1
    return year


def main():
    x = int(input())
    print(solve(x))


if __name__ == '__main__':
    main()
