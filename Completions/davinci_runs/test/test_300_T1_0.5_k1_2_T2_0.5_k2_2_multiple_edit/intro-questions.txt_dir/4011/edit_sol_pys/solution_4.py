
def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    p = [0] + p

    for i in range(n):
        a[i] = p[a[i]]

    a = ' '.join(map(str, a))

    print(a)

if __name__ == '__main__':
    main()
