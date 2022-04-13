

def main():
    n = int(input())
    a = list(map(float, input().split()))
    ans = 0
    for i in range(n):
        ans += 1/a[i]
    print(1/ans)

if __name__ == '__main__':
    main()
