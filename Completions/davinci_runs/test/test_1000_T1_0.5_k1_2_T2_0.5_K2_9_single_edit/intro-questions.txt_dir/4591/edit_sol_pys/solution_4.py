
import sys

def main():
    a, b, c, x, y = [int(x) for x in sys.stdin.readline().split()]

    cost = 0

    if A + B > 2 * C:
        if X > Y:
            cost += 2 * c * x
            y -= x
            x = 0
        else:
            cost += 2 * c * y
            x -= y
            y = 0

    cost += a * x
    cost += b * y

    print(cost)

if __name__ == "__main__":
    main()
