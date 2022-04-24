

def main():
    a, b, c = [int(x) for x in input().split()]  # read three numbers

    if a + b + c > 7:  # if the sum is greater than 7
        print(7)
    else:  # if the sum is not greater than 7
        print(a + b + c)

if __name__ == '__main__':
    main()
