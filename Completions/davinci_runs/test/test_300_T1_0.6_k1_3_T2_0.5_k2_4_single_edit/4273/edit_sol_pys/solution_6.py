
import sys
import itertools

def main():
    N = int(input())
    names = [input() for _ in range(N)]
    marc_names = []
    for name in names:
        if name[0] in ["M", "A", "R", "C", "H"]:
            marc_names.append(name)
    marc_names.sort()
    ans = 0
    for c in itertools.combinations(marc_names, 3):
        if len(set(map(lambda x:x[0], c))) == 3:
            ans += 1
    print(ans)
