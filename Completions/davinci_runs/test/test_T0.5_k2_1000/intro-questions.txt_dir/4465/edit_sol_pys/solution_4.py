

def main():
    a, b, c = map(int, input().split())
    print(a * b * c)
    print((a * b + b * c + c * a) * 2)

if __name__ == '__main__':
    main()
