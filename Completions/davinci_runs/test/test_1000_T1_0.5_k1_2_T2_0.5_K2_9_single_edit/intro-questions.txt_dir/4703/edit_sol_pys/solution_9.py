
from itertools import combinations

def main():
    S = input()
    ans = 0
    for i in range(1, len(S)):
        for c in combinations(range(len(S) - 1), i):
            tmp = S
            for j in c:
                tmp = tmp[:j+1] + '+' + tmp[j+1:]
            ans += sum(map(int, tmp.split('+')))

    print(ans)

if __name__ == '__main__':
    main()
