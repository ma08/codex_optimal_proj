

def main():
    n = int(input())
    rolls = list(map(int, input().split()))  # list of rolls
    max_roll = max(rolls)  # max roll
    if rolls.count(max_roll) == 1:  # if the max roll is unique
        print(rolls.index(max_roll) + 1)  # print the index of the max roll
    else:
        print("none")

if __name__ == "__main__":
    main()
