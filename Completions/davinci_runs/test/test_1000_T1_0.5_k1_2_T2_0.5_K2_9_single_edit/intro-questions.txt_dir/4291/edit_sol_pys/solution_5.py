

def main():
    n, q = map(int, input().split())
    s = input()
    lr = [list(map(int, input().split())) for _ in range(q)]  # 開始地点と終了地点を格納するリスト
    ans = []
    for i in range(q):
        ans.append(s[lr[i][0]-1:lr[i][1]].count("AC"))  # 開始地点と終了地点を指定して、ACの個数を数える
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
