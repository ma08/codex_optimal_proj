

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    c = 0
    i = 0
    while i < n:
        if a[i] == a[i + 1]:
            c += 1
            i += 2
        else:
            i += 1
    print(c)

if __name__ == '__main__':
    main()
