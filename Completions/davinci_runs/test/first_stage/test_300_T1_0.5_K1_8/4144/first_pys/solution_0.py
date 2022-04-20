

def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            ans += 10**((i-1)//2)
        else:
            ans += 10**((i-2)//2)
    print(ans % (10**9 + 7))

if __name__ == '__main__':
    main()