
#
def main():
    q = int(input())
    for _ in range(q):
        n, a, b = map(int, input().split())
        if b < 2*a:
            print((n//2) * b + (n%2) * a)
        else:
            print(n*a)

if __name__ == '__main__':
    main()
