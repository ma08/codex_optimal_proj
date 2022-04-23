
def main():
    n, q = map(int, input().split())  # n:文字数, q:クエリの数
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]  # クエリの左端と右端
    ans = []
    for i in range(q):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))  # クエリの左端から右端までの文字列の中に"AC"がいくつあるかをカウント
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
