

def main():
    a, b = [int(x) for x in input().split()]

    if a + b > 7:
        print(7)
    else:
        print(a + b)

if __name__ == '__main__':
    main()
