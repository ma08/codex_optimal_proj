

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a > 20 or a < 1 or b > 20 or b < 1:
        print(-1)
        return -1
    print(a * b)

if __name__ == '__main__':
    main()
