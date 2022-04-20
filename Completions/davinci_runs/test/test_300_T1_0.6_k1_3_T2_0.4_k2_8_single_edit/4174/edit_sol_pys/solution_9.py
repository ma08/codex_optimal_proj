

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n):
        if a[i-1] == a[i]:
            print('NO')
            exit()
    print('YES')

if __name__ == '__main__':
    main()
