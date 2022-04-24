

def main():
    a, b, c = [int(x) for x in input().split()]

    if a + b + c > 9:
        print(9)
    else:
        print(a + b + c)

if __name__ == '__main__':
    main()
