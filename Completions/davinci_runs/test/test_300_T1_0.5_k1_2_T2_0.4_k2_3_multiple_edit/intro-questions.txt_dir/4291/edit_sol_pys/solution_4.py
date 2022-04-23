# https://atcoder.jp/contests/abc087/tasks/arc090_a

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]
    for i in range(q):  # リスト内包表記で書き直せる
        print(s[lr[i][0]-1:lr[i][1]].count("AC"))

    # リスト内包表記
    for i in [s[lr[i][0]-1:lr[i][1]].count("AC") for i in range(q)]:
        print(i)

if __name__ == '__main__':
    main()
