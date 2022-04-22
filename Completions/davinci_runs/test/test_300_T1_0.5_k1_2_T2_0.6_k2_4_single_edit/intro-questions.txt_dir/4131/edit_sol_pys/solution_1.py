from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)



def main():
    N, M = map(int, input().split())
    # prefecture_cities = [[] for _ in range(N)]
    prefecture_cities = defaultdict(list)  # key が存在しないときに空リストを返す dict
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_cities[P].append(Y)
    for P, cities in prefecture_cities.items():
        cities.sort()
        for i, city in enumerate(cities, 1):
            print('{:>06}{:>06}'.format(P, i))

if __name__ == '__main__':
    main()
