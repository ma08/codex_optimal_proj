
import sys

def main():
    # reads in data
    a, b, c = [int(x) for x in sys.stdin.readline().split()]

    # calculates the maximum number of days the cat can eat in a trip
    # without additional food purchases.
    if a <= b and a <= c:
        days = a // 2
    elif b <= a and b <= c:
        days = b
    elif c <= a and c <= b:
        days = c // 2
    else:
        days = min(a, b, c)

    # prints the result.
    print(days * 7)

if __name__ == "__main__":
    main()
