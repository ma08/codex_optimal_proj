
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(a[n//2-1])
        return
    print(a[n//2])
    return

if __name__ == '__main__':
    main()
