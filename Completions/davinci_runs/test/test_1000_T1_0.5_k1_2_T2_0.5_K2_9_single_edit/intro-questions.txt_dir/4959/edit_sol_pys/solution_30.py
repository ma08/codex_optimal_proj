

def main():
    e, f, c = map(int, input().split(' '))
    n = (e + f) // c
    left = (e + f) % c
    while n + left >= c:
        n += left // c
        left = (left % c) + (left // c)
    print(n)

if __name__ == '__main__':
    main()
