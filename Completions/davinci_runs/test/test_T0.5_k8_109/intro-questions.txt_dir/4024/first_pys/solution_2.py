

# Solution

def main():
    n, k = list(map(int, input().split()))
    s = input()

    if k > n:
        print(-1)
        return
    
    if k == n:
        print(0)
        return

    print(n*k - (n*(n+1)//2))


if __name__ == "__main__":
    main()