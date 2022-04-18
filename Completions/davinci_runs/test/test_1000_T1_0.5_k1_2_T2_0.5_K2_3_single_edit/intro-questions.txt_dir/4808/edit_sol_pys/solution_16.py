

def find_days(n, days, snow):
    i = 0
    while i < n and days[i] > snow:
        i += 1
    return i


def main():
    n, days = int(input()), list(map(int, input().split()))
    print("It hadn't snowed this early in {} years!".format(find_days(n, days)))


if __name__ == "__main__":
    main()
