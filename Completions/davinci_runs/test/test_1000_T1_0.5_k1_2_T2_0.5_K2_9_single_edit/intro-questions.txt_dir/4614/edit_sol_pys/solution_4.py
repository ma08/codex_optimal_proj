
def main():
    a, b, c = map(int, input().split())
    if a == b and b != c:
        print(c)
    elif a == c and a != b:
        print(b)
    else:
        print(a)

if __name__ == '__main__':
    main()
