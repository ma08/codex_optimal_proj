
from sys import stdin

def main():
    n = int(stdin.readline())
    lines = list(map(int, stdin.readline().split()))
    lines.sort()
    if n % 2 == 0:
        lines.reverse()
    print(" ".join([str(x) for x in lines]))

if __name__ == "__main__":
    main()
