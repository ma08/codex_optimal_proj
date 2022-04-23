

def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    res = -1
    for i in range(n):
        if res < sum(a[i:i+x+1]):
            res = sum(a[i:i+x+1])
    print(res)

if __name__ == '__main__':
    main()
