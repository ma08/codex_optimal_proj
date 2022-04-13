

def find_days(n, days):
    for i in range(n):
        if days[i] < days[-1]:
            return i
    return n


def main():
    n, days = int(input()), list(map(int, input().split()))
    print("It had not snowed this early in {} years!".format(find_days(n, days)))


if __name__ == "__main__":
    main()
