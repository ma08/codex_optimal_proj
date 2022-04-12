def get_input():
    n = int(input())

    trips = {}
    for i in range(n):
        country, year = input().split()
        if country in trips:
            trips[country].append(int(year))
        else:
            trips[country] = [int(year)]

    q = int(input())
    for i in range(q):
        country, k = input().split()
        print(sorted(trips[country])[int(k)-1])


if __name__ == '__main__':
    get_input()
