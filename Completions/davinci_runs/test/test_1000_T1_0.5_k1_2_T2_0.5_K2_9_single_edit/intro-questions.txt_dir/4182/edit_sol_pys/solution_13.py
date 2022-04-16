import sys

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    if x >= y:
        print("War")
        sys.exit()

    print("War")

if __name__ == '__main__':
    main()
