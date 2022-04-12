import sys

def hailstone(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + hailstone(n // 2)
    else:
        return n + hailstone(3 * n + 1)

def main():
    n = int(sys.stdin.readline().rstrip())
    print(hailstone(n))

if __name__ == "__main__":
    main()
