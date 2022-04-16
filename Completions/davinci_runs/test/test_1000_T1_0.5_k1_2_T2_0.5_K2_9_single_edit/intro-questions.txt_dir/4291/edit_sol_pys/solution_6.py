
def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]
    ans = []
    for i in range(q):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))  # 文字列のスライスで指定したインデックスの部分文字列を取得
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
