

def main():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if a[0] > b[1]:
        print(-1)
    else:
        print(b[1] - a[0])

if __name__ == '__main__':
    main()
