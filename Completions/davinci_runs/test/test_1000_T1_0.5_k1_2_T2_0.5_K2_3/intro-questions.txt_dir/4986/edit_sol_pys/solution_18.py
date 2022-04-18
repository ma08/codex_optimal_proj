
def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0
    for i in range(n):
        if a[i] % 2 == 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
