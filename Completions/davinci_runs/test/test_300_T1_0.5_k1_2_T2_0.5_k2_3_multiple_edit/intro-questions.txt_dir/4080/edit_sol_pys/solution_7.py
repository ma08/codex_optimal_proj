

def main():
    n = input()

    a = map(int, raw_input().split())

    b = map(int, raw_input().split())

    c = map(int, raw_input().split())

    a.sort()
    b.sort()
    c.sort()

    s = 0
    for i in range(n):
        s += b[i] * c[n-i-1]

    print s

if __name__ == "__main__":
    main()
