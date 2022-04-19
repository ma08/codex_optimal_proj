

def main():
    N, M = map(int, input().split())
    prefecture_cities = [[] for _ in range(N)]
    # prefecture_cities = defaultdict(list)
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_cities[P - 1].append(Y)
    for i, cities in enumerate(prefecture_cities):
        cities.sort()  # 市町村を登録順にソートする
        for j, city in enumerate(cities, 1):
            print('{:>06}{:>06}'.format(i + 1, j))

if __name__ == '__main__':
    main()
