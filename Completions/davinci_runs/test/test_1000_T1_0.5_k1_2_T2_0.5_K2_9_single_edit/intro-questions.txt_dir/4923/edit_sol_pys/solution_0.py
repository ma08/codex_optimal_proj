

def main():
    n = int(input())
    rolls = list(map(int, input().split()))
    maximum = max(rolls)
    if rolls.count(maximum) == 1:
        print(rolls.index(maximum) + 1)
    else:
        print("none")

if __name__ == "__main__":
    main()
