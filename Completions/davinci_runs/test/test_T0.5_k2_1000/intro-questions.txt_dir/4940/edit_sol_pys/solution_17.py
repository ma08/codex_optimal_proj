

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    ans = 0
    for i in range(n-1):
        if a[i] == a[i+1] - 1:
            ans += c[a[i]-1]
    print(sum(b) + ans)

if __name__ == '__main__':
    main()
