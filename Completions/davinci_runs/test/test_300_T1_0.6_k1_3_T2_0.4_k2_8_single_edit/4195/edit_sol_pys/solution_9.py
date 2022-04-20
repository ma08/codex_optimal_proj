
def main():
    """ main """
    d, n = [int(i) for i in input().split()] # split input and convert to int
    if d == 0:
        print(n) # if d is 0, print n
    else:
        print(100*n) # if d is 1, print 100*n

if __name__ == "__main__":
    main()
