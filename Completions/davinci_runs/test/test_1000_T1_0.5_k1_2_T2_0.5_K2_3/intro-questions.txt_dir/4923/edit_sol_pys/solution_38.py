
from collections import Counter

def main():
    n = int(input())
    rolls = list(map(int, input().split()))
    counts = Counter(rolls)
    max_duplicate = max(counts)
    if counts[max_duplicate] == 1:
        print(rolls.index(max_duplicate) + 1)
    else:
        print("none")

if __name__ == "__main__":
    main()
