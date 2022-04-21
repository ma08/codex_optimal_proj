
def main():
    n = int(input())
    h = list(map(int, input().split()))  # a list of integers
    ans = 0
    while n > 0:  # loop until n = 0
        n -= 1  # decrease n by 1
        if n == 0:  # check if n = 0
            ans += 1
            break
        if h[n] >= h[n-1]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
