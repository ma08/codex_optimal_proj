

from collections import Counter

def main():
    n = int(input())
    rolls = list(map(int, input().split()))
    counts = Counter(rolls)
    max_count = max(counts.values())
    if max_count == 1:
        for roll in counts:
            if counts[roll] == max_count:
                print(rolls.index(roll) + 1)
                break
    else:
        print("none")

if __name__ == "__main__":
    main()
