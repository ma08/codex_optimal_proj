

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n - 1)
    for i in range(n - 1):
        b[i] = a[i + 1] - a[i]
    if 1 in b or -1 in b:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()