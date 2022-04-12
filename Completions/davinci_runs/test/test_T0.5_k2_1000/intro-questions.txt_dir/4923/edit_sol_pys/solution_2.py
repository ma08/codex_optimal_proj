

def main():
    n = int(input())
    rolls = list(map(int, input().split()))
    max_rolls = max(rolls)
    if rolls.count(max_rolls) == 1:
        print(rolls.index(max_rolls) + 1)
    else:
        print("none")

if __name__ == "__main__":
    main()
