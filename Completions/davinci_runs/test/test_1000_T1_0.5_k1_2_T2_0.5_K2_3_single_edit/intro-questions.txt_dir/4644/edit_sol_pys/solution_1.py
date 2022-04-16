

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        if sum(arr) % 2 == 0:
            print("NO")
        else:
            print("YES")


if __name__ == '__main__':
    main()
