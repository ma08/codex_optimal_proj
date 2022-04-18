

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("NO" if sum(a) % 2 == 0 else "YES")


if __name__ == '__main__':
    main()
