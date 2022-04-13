
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0.0
    for i in range(n):
        ans += 1.0/a[i]
    print(1.0/ans)

if __name__ == '__main__':
    main()
