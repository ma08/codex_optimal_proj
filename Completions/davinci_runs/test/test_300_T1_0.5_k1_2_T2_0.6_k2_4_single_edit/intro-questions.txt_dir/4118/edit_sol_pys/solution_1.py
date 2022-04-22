

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if not 1 <= a <= 20 or not 1 <= b <= 20:
        print(-1)
        return
    print(a * b)

if __name__ == '__main__':
    main()
