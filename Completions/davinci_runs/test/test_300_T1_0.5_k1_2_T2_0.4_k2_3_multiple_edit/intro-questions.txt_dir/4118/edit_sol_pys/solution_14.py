

def main():
    a, b, c = input().split()
    a = int(a) - 1
    b = int(b) - 1
    c = int(c) - 1
    if a > 100 or a < 0 or b > 100 or b < 0 or c > 100 or c < 0:
        print(-1)
        return
    print(a * b * c)

if __name__ == '__main__':
    main()
