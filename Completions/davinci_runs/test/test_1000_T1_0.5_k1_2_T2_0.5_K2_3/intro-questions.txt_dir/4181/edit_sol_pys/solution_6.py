
def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(sum(min(a[i], b[i]) for i in range(n)))

if __name__ == '__main__':
    main()
