

def main():
    n, r = map(int, input().split()) # n: プロジェクト数, r: 初期資金
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split()))) # i番目のプロジェクトの資金額とリターン
    projects.sort(key=lambda x: x[1]) # リターン額でソート
    for project in projects:
        if r >= project[0]: # 資金が足りていれば投資
            r += project[1]
            if r < 0: # 資金が足りなくなったら終了
                print("NO")
                return
    print("YES")

if __name__ == '__main__':
    main()
