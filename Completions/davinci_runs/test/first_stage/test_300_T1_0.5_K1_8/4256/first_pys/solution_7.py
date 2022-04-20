

def main():
    a, b, c = map(int, input().split())
    if b >= a:
        if b // a < c:
            print(b // a)
        else:
            print(c)
    else:
        print(0)

if __name__ == '__main__':
    main()