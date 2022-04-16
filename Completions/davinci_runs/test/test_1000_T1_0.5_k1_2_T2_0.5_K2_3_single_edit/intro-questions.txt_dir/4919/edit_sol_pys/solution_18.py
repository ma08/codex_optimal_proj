
import sys

def main():
    n = int(sys.stdin.readline())
    trips = {}
    for _ in range(n):
        if country not in trips:
            trips[country] = []
        country, year = sys.stdin.readline().split()
        if country in trips:
            trips[country].append(year)
    q = int(sys.stdin.readline())
    for _ in range(q):
        country, k = sys.stdin.readline().split()
        print(trips[country][int(k) - 1])

if __name__ == "__main__":
    main()
