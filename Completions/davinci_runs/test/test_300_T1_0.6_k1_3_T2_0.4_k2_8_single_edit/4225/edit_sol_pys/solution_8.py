import sys
sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    print(a)

if __name__ == '__main__':
    main()
