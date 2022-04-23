

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > 100 or a < 1 or b > 100 or b < 1:
        print(-1)
        return
    print(a * b)


if __name__ == '__main__':
    main()
