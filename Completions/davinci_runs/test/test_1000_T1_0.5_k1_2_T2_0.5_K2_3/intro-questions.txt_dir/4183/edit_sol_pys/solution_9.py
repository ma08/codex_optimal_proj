# AOJ 0036

def main():
    N = int(input())
    for i in range(N):
        x, y = map(int, input().split())
        if y % x == 0:
            print(y // x)
        else:
            print("NO")


if __name__ == '__main__':
    main()
