

def main():
    a, b = input().split(",")  # a is number of rows, b is number of columns
    a = int(a)  # convert to int
    b = int(b)  # convert to int
    if a > 20 or a < 1 or b > 20 or b < 1:  # check if a and b is valid
        print(-1)
        return
    print(a * b)  # print the number of squares

if __name__ == '__main__':
    main()
