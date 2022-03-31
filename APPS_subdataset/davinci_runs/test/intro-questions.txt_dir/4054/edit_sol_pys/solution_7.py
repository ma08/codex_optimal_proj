
import sys

def main():
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(sum(a) - max(a) - min(a))

main()
