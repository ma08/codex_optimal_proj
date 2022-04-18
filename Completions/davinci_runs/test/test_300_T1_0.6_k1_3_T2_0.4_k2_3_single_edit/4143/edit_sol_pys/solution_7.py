
def main():
    n = int(input())
    l = [int(input()) for _ in range(5)]

    l = [a, b, c, d, e]
    l.sort()

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
