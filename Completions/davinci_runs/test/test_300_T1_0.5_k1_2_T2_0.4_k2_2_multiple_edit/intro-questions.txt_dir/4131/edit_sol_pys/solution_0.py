

def main():
    N, M = map(int, input().split())
    # prefecture_cities = [[] for _ in range(N)]  # list of lists
    prefecture_cities = defaultdict(list)  # 辞書
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_cities[P].append(Y)
    for P, cities in prefecture_cities.items():
        cities.sort()
        for i, city in enumerate(cities, 1):
            print('{:>06}{:>06}'.format(P, i))

if __name__ == '__main__':
    main()
