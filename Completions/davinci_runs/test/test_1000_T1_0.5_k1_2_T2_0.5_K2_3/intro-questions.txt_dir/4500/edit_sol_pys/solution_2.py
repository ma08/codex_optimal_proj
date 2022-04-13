
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if a[i] != (i + 1):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
