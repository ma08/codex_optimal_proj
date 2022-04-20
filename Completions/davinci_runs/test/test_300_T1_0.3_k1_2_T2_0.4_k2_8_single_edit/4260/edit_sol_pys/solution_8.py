

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] % 2 == 0:
            if a[i] % 3 == 0 or a[i] % 5 == 0:
                ans += 1
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
