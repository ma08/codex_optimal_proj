

def find_days(n, days):
    for i in range(n):
        if days[i] <= days[-1]:
            return i
    return n


def main():
    n = int(input())
    days = list(map(int, input().split()))
    print("It hadn't snowed this early in " +
          str(find_days(n, days)) + " years!")


if __name__ == "__main__":
    main()
