

def main():
    n = int(input())
    a = list(map(int, input()))
    t = list(map(int, input().split()))
    t = [0] + t

    for i in range(1, n+1):
        a[i-1] = t[a[i-1]]
    a = int(a)

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
