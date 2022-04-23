

def main():
    n = int(input())
    a = list(map(int, input().split()))
    t = list(map(int, input().split()))
    t = [0] + t

    for i in range(n):
        a[i] = t[int(a[i])]

    a = ''.join(a)

    print(a)

if __name__ == '__main__':
    main()
