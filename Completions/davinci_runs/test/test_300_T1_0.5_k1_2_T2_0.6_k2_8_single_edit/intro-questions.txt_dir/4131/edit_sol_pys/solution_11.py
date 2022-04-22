
def main():
    N, M = map(int, input().split())
    # prefecture_cities = [[] for _ in range(N)]
    prefecture_cities = {}
    for _ in range(M):
        P, Y = map(int, input().split())
        if P in prefecture_cities:
            prefecture_cities[P].append(Y)
        else:
            prefecture_cities[P] = [Y]
    for prefecture, cities in prefecture_cities.items():
        for i, city in enumerate(sorted(cities), 1):
            print('{:>06}{:>06}'.format(prefecture, i))

if __name__ == '__main__':
    main()
