def main():
    a, b, c = map(int, input().split())
    if a == b and a == c:
        print(a)
    elif a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(a)

if __name__ == '__main__':
    main()
