

def main():
    a, b, c = map(int, input().split())
    print(a * b * c)
    print(2 * (a * b + b * c + a * c))

if __name__ == '__main__':
    main()
