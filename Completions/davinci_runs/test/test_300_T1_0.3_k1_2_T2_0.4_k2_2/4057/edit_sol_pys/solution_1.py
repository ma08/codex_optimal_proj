

from sys import stdin

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    a = set(a)
    print(len(a))

if __name__ == "__main__":
    main()
