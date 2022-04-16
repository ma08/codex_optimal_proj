

def main():
    n = int(input())
    rolls = list(map(int, input().split()))
    maxRoll = max(rolls)
    if rolls.count(maxRoll) == 1 and maxRoll != 1:
    elif maxRoll == 1:
        print("none")
        print(rolls.index(maxRoll) + 1)
    else:
        print("many")

if __name__ == "__main__":
    main()
