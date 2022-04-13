
from collections import Counter

def main():
    n = int(input())
    rolls = list(map(int, input().split()))
    counts = Counter(rolls)
    max_roll = max(rolls)
    if counts[max_roll] == 1:
        print(rolls.index(max_roll) + 1)
    else:
        print("none")

if __name__ == "__main__":
    main()
