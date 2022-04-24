from collections import defaultdict

def main():
    N, M = map(int, input().split())
    # prefectures_cities = [[] for _ in range(N)]
    prefectures_cities = defaultdict(list)
    for _ in range(M):
        P, Y = map(int, input().split())
        prefectures_cities[P].append(Y)
    for P, cities in prefectures_cities.items():
        cities.sort()
        for i, city in enumerate(cities, 1):
            print('{:>06}{:>06}'.format(P, i))

if __name__ == '__main__':
    main()
