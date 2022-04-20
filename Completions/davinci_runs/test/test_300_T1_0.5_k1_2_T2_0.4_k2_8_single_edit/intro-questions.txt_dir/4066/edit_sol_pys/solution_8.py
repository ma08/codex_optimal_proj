

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            print(a[i], a[i + 1])
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()
