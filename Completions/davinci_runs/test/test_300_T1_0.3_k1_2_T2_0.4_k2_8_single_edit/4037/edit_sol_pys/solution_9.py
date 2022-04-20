

def main():
    n, r = map(int, input().split())  # n はプロジェクト数, r は残りの予算
    projects = []
    for _ in range(n):
        projects.append(list(map(int, input().split())))  # [0] は費用, [1] は価値
    projects.sort(key=lambda x: x[1])  # 価値の降順にソート
    count = 0
    for project in projects:
        if r >= project[0]:  # 予算が足りる場合
            r += project[1]
            count += 1
    print(count)

if __name__ == '__main__':
    main()
