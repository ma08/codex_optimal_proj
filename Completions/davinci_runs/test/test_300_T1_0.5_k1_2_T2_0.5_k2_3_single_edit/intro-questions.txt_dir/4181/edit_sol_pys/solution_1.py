

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    b = list(map(int, input().split()))[:n]
    print(sum(min(a[i], b[i]) for i in range(n)) + min(a[n-1], b[n-1]))

if __name__ == '__main__':
    main()
