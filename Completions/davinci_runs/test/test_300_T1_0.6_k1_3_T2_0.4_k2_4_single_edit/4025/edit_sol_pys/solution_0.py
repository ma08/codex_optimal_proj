

def main():
    a, b, c, d = [int(x) for x in input().split()]

    if a + b + c + d > 9:
        print(9)
    else:
        print(a + b + c + d)

if __name__ == '__main__':
    main()
