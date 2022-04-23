

def main():
    # read input and convert to integer
    x, a = map(int, input().split())

    # compare the two values and print the result.
    if x < a:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()
