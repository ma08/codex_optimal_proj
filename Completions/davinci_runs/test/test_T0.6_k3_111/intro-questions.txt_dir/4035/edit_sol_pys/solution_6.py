

def main():
    n = int(input())
    a = list(map(int, input().split(' ')))
    a.sort()
    for i in range(n):
        if i%2 == 0:
            print(a[i//2], end=' ')
        else:
            print(a[n//2+i//2], end=' ')

if __name__ == '__main__':
    main()
