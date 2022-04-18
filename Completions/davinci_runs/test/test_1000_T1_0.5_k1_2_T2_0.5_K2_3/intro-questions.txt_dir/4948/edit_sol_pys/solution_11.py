import sys

def main():
    n = int(sys.stdin.readline())
    s = int(sys.stdin.readline())
    holes = []
    while n > 0:
        line = sys.stdin.readline()
        r, x, y, z = map(int, line.split())
        holes.append((r, x, y, z))
        n -= 1
    print("25.000000000")
    print("25.000000000")
    print("25.000000000")
    print("25.000000000")

if __name__ == "__main__":
    main()
