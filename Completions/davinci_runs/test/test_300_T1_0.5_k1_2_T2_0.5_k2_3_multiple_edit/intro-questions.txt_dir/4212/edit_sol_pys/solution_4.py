

def main():
    n = int(input())
    d = [int(input()) for _ in range(n)]
    d.sort()
    if n % 2 == 0:
        ans = d[n//2] - d[n//2-1] + 1
    else:
        ans = 0

    print(ans)

if __name__ == '__main__':
    main()
