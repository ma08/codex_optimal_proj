

from collections import defaultdict

def main():
    n = int(input())
    s = input()

    # count the number of times each character appears
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1

    # build the coloring
    coloring = []
    for c in s:
        if counts[c] == 0:
            continue
        counts[c] -= 1
        coloring.append(c)
    print(len(coloring))
    print(*coloring)


if __name__ == "__main__":
    main()