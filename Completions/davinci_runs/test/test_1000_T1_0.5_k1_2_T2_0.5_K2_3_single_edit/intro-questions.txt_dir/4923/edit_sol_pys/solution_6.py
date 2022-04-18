

from collections import Counter, defaultdict

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        rolls = list(map(int, input().split()))
        counts = Counter(rolls)
        max_roll = max(counts)
        if counts[max_roll] == 1:
            print(rolls.index(max_roll) + 1)
        else:
            print("none")

if __name__ == "__main__":
    main()
