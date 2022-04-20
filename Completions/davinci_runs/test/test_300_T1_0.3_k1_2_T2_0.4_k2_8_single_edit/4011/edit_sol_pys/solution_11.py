

def main():
    n = int(input())
    a = input()
    a = [int(a[i]) for i in range(n)]
    a.sort()
    for i in range(n):
        print(a[i], end=' ')

if __name__ == '__main__':
    main()
