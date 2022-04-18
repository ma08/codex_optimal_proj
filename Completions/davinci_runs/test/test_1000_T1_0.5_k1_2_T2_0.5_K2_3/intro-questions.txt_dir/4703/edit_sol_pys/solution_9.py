

from itertools import combinations

def calc(s):
    if '+' not in s:
        return int(s)
    return sum(map(int, s.split('+')))

def main():
    s = input()
    ans = 0
    for i in range(1, len(s) - 1):
        for c in combinations(range(len(s) - 1), i):
            tmp = s
            for j in c:
                tmp = tmp[:j+1] + '+' + tmp[j+1:]
            ans += calc(tmp)
    print(ans)

if __name__ == '__main__':
    main()
