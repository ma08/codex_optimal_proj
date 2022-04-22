from collections import defaultdict


def main():
    N, M = map(int, input().split())
    # prefecture_city = [[] for _ in range(N)]
    prefecture_city = defaultdict(list)
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_city[P].append(Y)
    for P, cities in prefecture_city.items():
        cities.sort()
        for i, city in enumerate(cities, 1):
            print('{:>06}{:>06}'.format(P, i))

if __name__ == '__main__':
    main()
