

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(a*b if 1 <= a <= 20 and 1 <= b <= 20 else -1)

if __name__ == '__main__':
    main()
