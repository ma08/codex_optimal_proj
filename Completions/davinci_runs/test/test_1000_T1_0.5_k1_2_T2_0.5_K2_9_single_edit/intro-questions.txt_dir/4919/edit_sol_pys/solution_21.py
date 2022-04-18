
import sys

def main():
    with open("test.txt") as f:
        n = int(f.readline())
        trips = {}
        for _ in range(n):
            country, year = f.readline().split()
            if country in trips:
                trips[country].append(year)
            else:
                trips[country] = [year]
        q = int(f.readline())
        for _ in range(q):
            country, k = f.readline().split()
            print(trips[country][int(k) - 1])

if __name__ == "__main__":
    main()
