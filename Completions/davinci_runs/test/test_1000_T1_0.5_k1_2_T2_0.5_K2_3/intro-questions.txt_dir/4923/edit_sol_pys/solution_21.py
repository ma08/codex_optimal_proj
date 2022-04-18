
def main():
    n = int(input())
    rolls = list(map(int, input().split()))
    max_roll = max(rolls)
    if rolls.count(max_roll) == 1:
        print(rolls.index(max_roll) + 1)
    else:
        print("none")

if __name__ == "__main__":
    main()
