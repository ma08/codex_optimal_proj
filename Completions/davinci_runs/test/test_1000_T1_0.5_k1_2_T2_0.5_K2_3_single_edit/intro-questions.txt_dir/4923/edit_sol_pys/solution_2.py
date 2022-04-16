

def main():
    _ = int(input())
    rolls = list(map(int, input().split()))
    maxRoll = max(rolls)
    if rolls.count(maxRoll) == 1:
        print(rolls.index(maxRoll) + 1)
    else:
        print("none")

if __name__ == "__main__":
    main()
