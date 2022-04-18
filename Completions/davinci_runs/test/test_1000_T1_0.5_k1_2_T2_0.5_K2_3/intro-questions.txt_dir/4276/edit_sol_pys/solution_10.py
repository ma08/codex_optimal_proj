
import sys

def main():
    n, t = map(int, sys.stdin.readline().split())
    min_price = t + 1
    for _ in range(n):
        price, time = map(int, sys.stdin.readline().split())
        if time <= t:
            min_price = min(min_price, price)
    if min_price > t:
        print("TLE")
    else:
        print(min_price)

if __name__ == "__main__":
    main()
