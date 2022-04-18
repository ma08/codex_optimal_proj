

def main():
    a, b, c = [int(x) for x in input().split()]

    if a + b + c > 21:
        print(21)
    else:
        print(a + b + c)

if __name__ == '__main__':
    main()
