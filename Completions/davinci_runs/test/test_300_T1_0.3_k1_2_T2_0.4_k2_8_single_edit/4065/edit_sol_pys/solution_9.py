

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    cur = 0
    for i in range(n):
        if a[i] > cur * 2:
            cur = a[i]
            ans += 1
        else:
            cur = a[i]
    print(ans)

if __name__ == "__main__":
    main()
