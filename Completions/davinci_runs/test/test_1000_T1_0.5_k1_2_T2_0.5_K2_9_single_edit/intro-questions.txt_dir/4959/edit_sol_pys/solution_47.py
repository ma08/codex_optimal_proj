
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    res = 0
    for i in range(n):
        res += b[a[i]-1]
        if i > 0 and a[i-1]+1 == a[i]:
            res += c[a[i-1]-1]
    print(res)

if __name__ == '__main__':
    main()
