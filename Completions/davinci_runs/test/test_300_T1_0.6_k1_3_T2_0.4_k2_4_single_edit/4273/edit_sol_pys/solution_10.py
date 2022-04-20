
import sys
import itertools

def main():
    N = int(input())
    names = [input() for _ in range(N)]
    marc_names = sorted(filter(lambda x:x[0] in ["M", "A", "R", "C", "H"], names))
    ans = 0
    for c in itertools.combinations(marc_names, 3):
        if len(set(map(lambda x:x[0], c))) == 3:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
