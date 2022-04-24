import sys



def main():
    n = int(sys.stdin.readline())
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    d = int(sys.stdin.readline())
    e = int(sys.stdin.readline())

    l = [a, b, c, d, e]
    l.sort()

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
