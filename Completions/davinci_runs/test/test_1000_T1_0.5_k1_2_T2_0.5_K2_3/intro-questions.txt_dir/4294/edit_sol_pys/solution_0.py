

def main():
    # read input
    x, a = [int(i) for i in input().split()] # split input into two variables

    # compare the two values and print the result.
    if x < a:
        print(0)
    else:
        print(10)

if __name__ == '__main__':
    main()
