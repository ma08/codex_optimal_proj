

def main():
    a, b, c = [int(input()) for _ in range(3)]

    if a + b + c > 7:
        print(7)
    else:
        print(a + b + c)

if __name__ == '__main__':
    main()
