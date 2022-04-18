
def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            ans += 1
        else:
            ans += 1
            break
    else:
        if h[n-2] <= h[n-1]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
