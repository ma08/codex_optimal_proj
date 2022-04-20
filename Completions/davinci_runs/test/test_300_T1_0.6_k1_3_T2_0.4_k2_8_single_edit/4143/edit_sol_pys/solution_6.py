

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    if n <= a[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
