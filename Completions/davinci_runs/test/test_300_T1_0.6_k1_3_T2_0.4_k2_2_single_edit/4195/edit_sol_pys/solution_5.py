

def main():
    """ main """
    d, n = [int(i) for i in input().split()]  # split input into two variables
    if d == 0:
        print(n)
    else:
        print(100*n)  # print 100 times n

if __name__ == "__main__":
    main()
