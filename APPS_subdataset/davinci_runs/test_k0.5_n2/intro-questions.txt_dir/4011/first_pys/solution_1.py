

def main():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    res = 0
    for i in range(n):
        res = res * 10 + f[int(a[i]) - 1]

    print(res)

if __name__ == "__main__":
    main()