

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        for i in range(n-2):
            if a[i] == a[i+1]:
                print('YES')
                break
            if a[i] == a[i+2]:
                print('YES')
                break
        else:
            print('NO')

if __name__ == '__main__':
    main()