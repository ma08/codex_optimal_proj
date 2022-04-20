

def main():
    a, b, c = [int(x) for x in input().split()]

    print(a + b + c) if a + b + c < 7 else print(7)

if __name__ == '__main__':
    main()
