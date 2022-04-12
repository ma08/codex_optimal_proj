
from sys import stdin

def main():
    n = int(stdin.readline())
    line = list(map(int, stdin.readline().split()))
    line.sort(reverse=True)
    if n % 2 == 0:
        line = line[1::2] + line[::2]
    print(" ".join([str(x) for x in line]))

if __name__ == "__main__":
    main()
