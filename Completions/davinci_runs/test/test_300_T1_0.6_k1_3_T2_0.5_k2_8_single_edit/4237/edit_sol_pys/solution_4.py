

from math import gcd

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    if len(set(S)) == N:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
