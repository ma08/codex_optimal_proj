
def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n-1, 0, -1):
        if h[i] >= h[i-1]:
            ans += 1
            break
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
