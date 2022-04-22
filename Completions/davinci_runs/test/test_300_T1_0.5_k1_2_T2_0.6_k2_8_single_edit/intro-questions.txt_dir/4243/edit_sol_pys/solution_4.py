import sys
sys.setrecursionlimit(1000000)

def main():
    x,y = map(int, input().split())
    print(x//y)
    print(x%y)
    print(float(x/y))

if __name__ == '__main__':
    main()
