
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[0]
    for i in range(1, n):
        ans = (ans + a[i]) / 2
    print(ans)

if __name__ == '__main__':
    main()
