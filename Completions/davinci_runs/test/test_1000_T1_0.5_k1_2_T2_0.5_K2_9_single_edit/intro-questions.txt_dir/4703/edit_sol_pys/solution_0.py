
import sys
from itertools import combinations


def calc(s):
    if '+' not in s:
        return int(s)
    s = s.split('+')
    return sum(map(int, s))

def main():
    s = sys.stdin.readline().rstrip()
    ans = 0
    for i in range(1, len(s)):
        for c in combinations(range(len(s) - 1), i):
            tmp = s
            for j in c:
                tmp = tmp[:j+1] + '+' + tmp[j+1:]
            ans += calc(tmp)
    print(ans)

if __name__ == '__main__':
    main()
