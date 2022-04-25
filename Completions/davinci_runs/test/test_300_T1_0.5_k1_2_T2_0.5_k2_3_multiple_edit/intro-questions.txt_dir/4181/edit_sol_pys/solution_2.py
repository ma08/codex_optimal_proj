

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(sum(min(a[i], b[i]) for i in range(n)) - min(a[n-1], b[n-1]))

if __name__ == '__main__':
    main()
