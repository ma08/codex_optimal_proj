

def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    ans = 0
    for i in range(n):
        if a[i] != (i + 1):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
