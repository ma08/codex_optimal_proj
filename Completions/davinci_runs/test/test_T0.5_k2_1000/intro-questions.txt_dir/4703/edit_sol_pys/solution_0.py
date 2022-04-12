from itertools import combinations

def calc(s):
    if '+' not in s:
        return int(s)
    s = s.split('+')
    return sum(map(int, s))

def main():
    s = input()
    ans = 0
    for i in range(1, len(s)):  # 1つ以上の+を追加する
        for c in combinations(range(len(s) - 1), i):  # i個の+を追加する
            tmp = s
            for j in c:  # j番目の+を追加する
                tmp = tmp[:j+1] + '+' + tmp[j+1:]
            ans += calc(tmp)
    print(ans)

if __name__ == '__main__':
    main()
