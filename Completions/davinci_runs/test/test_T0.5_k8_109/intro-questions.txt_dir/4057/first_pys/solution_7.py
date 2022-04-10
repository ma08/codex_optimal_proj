

def main():
    n = int(input())
    a = list(map(int, input().split()))
    coins = set(a)
    print(len(coins))


if __name__ == "__main__":
    main()