

from sys import stdin

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(set(a))
    print(len(b))

if __name__ == "__main__":
    main()
