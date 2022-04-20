
from collections import defaultdict
import sys
import itertools

def main():
    n = int(input())
    d = defaultdict(int)
    for _ in range(n):
        s = input()
        d[s[0]] += 1
    ans = 0
    for c in itertools.combinations(marc_names, 3):
        if len(set(map(lambda x:x[0], c))) == 3:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
