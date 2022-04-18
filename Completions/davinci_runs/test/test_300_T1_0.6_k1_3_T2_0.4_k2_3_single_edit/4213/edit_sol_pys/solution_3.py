

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())
    print(sum([x == a * i + b * j + c * k for i in range(x // a + 1) for j in range(x // b + 1) for k in range(x // c + 1)]))

if __name__ == '__main__':
    main()
