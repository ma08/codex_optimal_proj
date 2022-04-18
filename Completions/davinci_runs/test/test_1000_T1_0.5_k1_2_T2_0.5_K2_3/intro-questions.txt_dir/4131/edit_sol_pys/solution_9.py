from collections import defaultdict

def main():
    N, M = map(int, input().split())
    prefecture_city = defaultdict(list)
    for _ in range(M):
        P, Y = map(int, input().split())
        prefecture_city[P].append(Y)
    for P, city in prefecture_city.items():
        city.sort()
        for i, city in enumerate(city, 1):
            print('{:>06}{:>06}'.format(P, i))

if __name__ == '__main__':
    main()
