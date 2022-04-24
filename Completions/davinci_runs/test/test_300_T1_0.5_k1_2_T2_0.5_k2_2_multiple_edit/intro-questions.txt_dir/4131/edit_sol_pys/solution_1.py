

def main():
    N, M = map(int, input().split())
    # prefecture_cities = [[] for _ in range(N)] # これだと、都道府県ごとに空配列をN個作ってしまう。こっちのほうが、都道府県ごとに空配列を作るときにその分だけメモリを使う
    prefecture_cities = defaultdict(list)
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_cities[P].append(Y)
    for P, cities in prefecture_cities.items():
        cities.sort()
        for i, city in enumerate(cities, 1):
            print('{:>06}{:>06}'.format(P, i))

if __name__ == '__main__':
    main()
