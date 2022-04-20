
def main():
    n = int(input())
    h = list(map(int, input().split()))[::-1]
    ans = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            ans += 1
        elif h[i] < h[i+1]:
            break
    print(ans)

if __name__ == '__main__':
    main()
