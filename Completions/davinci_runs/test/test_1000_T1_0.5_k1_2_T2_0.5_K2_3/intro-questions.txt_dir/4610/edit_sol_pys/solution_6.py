

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    c = list(map(int, input().split()))[:n-1]
    print(sum(b) + sum(c[a[i]-1] for i in range(n-1) if a[i]+1 == a[i+1]))


if __name__ == '__main__':
    main()
