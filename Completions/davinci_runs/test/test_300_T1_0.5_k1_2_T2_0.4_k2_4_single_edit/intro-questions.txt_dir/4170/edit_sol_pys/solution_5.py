
def main():
    n = int(input())
    h = list(map(int, input().split())) # list object
    ans = 0
    while n > 0: # while loop
        n -= 1
        if n == 0: # if statement
            ans += 1
            break
        if h[n] >= h[n-1]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
