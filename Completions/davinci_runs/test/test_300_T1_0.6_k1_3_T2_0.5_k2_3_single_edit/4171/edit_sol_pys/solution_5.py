
def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    i = 0
    while a[i] < a[n-1]:
        a[i] = a[i]//2
        i += 1
    print(i)


if __name__ == '__main__':
    main()
