from collections import defaultdict

def main():
    N, M = map(int, input().split())
    prefecture_cities = defaultdict(list)
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_cities[P-1].append(Y)
    for P, cities in enumerate(prefecture_cities):
        cities.sort()
        for i, city in enumerate(cities):
            print('{:>06}{:>06}'.format(P+1, i+1))

if __name__ == '__main__':
    main()
