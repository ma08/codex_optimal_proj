

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if sum(a) % 2 != 0:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
