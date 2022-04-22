from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(10**7)
INF = 10**10
MOD = 10**9 + 7


def read_ints(): return list(map(int, input().split()))
def read_strs(): return list(input().split())

def main():
    T, X = read_ints()
    print(T / X)

if __name__ == '__main__':
    main()
