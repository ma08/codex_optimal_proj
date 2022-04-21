

def main():
    N, M = map(int, input().split())
    prefecture_cities = [[] for _ in range(N)]
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_cities[P - 1].append(Y)
    for P, cities in enumerate(prefecture_cities):
        cities = sorted(cities)
        for i, city in enumerate(cities):
            print('{:>06}{:>06}'.format(P, i))

if __name__ == '__main__':
    main()
