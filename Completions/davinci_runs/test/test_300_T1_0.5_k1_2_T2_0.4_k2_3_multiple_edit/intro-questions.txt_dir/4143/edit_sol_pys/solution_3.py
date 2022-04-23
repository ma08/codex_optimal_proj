import sys
input = sys.stdin.readline


def main():
    N = int(input())
    A, B, C, D, E = [int(i) for i in input().split()]

print(minute_needed(N))
