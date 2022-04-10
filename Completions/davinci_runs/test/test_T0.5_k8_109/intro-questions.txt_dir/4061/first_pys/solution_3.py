

# TODO: Solve with dynamic programming

import sys

def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    # Build suffix array
    suffixes = []
    for i in range(len(s)):
        suffixes.append(s[i:])

    # Sort suffixes
    suffixes.sort()

    # Build LCP array
    lcp = [0] * len(s)
    for i in range(1, len(s)):
        j = 0
        while suffixes[i][j] == suffixes[i-1][j]:
            j += 1
        lcp[i] = j

    print(lcp)


if __name__ == "__main__":
    main()