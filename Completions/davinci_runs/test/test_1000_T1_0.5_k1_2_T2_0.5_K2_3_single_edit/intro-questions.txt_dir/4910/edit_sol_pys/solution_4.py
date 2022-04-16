
import sys
from collections import Counter


def main():
    n = int(input())
    costumes = Counter()
    for i in range(n):
        costume = sys.stdin.readline().strip()
        costumes[costume] += 1
    max_count = max(costumes.values())
    for costume, count in sorted(costumes.items()):
        if count == max_count:
            print(costume, count)

if __name__ == "__main__":
    main()
