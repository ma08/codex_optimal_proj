

def main():
    n = int(input())
    a = list(map(int, input().split())) + [0]
    b = list(map(int, input().split())) + [0]
    ans = 0
    for i in range(n):
        ans += min(a[i], b[i])
        ans += min(a[i+1], b[i]-min(a[i], b[i]))
    print(ans)

if __name__ == '__main__':
    main()
