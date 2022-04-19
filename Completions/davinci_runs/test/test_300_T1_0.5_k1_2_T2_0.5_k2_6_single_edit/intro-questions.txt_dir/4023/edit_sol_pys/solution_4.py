

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if not a[i] % 2 == 0:
            print(a[i])

if __name__ == '__main__':
    main()
