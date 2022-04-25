def main():
    num_rows, num_cols = input().split()  # num_rows is number of rows, num_cols is number of columns
    num_rows = int(num_rows)  # convert to int
    num_cols = int(num_cols)  # convert to int
    if num_rows > 20 or num_rows < 1 or num_cols > 20 or num_cols < 1:  # check if num_rows and num_cols is valid
        print(-1)
        return
    print(num_rows * num_cols)  # print the number of squares


def main():
    a, b = input().split()  # a is number of rows, b is number of columns
    a = int(a)  # convert to int
    b = int(b)  # convert to int
    if a > 20 or a < 1 or b > 20 or b < 1:  # check if a and b is valid
        print(-1)
        return
    print(a * b)  # print the number of squares

if __name__ == '__main__':
    main()
