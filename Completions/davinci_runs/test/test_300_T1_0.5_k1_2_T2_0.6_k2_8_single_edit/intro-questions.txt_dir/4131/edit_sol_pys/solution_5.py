

def main():
    N, M = map(int, input().split())
    prefecture_cities = [[] for _ in range(N)]
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_cities[P - 1].append(Y)
    for P, cities in prefecture_cities.items():
        cities.sort()
        for i, city in enumerate(cities):
            print('{:>06}{:>06}'.format(P + 1, i + 1))

if __name__ == '__main__':
    main()
