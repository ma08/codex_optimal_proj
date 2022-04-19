

from sys import stdin

def solve(n, a, b):
    return " ".join(map(str, [a + b, a * b]))

def main():
    n = int(stdin.readline().strip())
    a = stdin.readline().strip().split(" ")
    b = stdin.readline().strip().split(" ")
    print(solve(n, a, b))

if __name__ == "__main__":
    main()
