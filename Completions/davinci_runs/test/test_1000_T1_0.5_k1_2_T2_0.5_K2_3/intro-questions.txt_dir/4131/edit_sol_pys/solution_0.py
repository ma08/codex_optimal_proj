from collections import defaultdict

def main():
    N, M = map(int, input().split())  # N:都道府県数, M:市町村数
    prefecture_cities = defaultdict(list)  # key:都道府県番号, value:市町村数リスト
    for _ in range(M):
        P, Y = map(int, input().split())  # P:都道府県番号, Y:市町村番号
        prefecture_cities[P].append(Y)  # PでソートされたYを追加
    for P, cities in prefecture_cities.items():
        cities.sort()
        for i, city in enumerate(cities, 1):
            print('{:>06}{:>06}'.format(P, i))

if __name__ == '__main__':
    main()
