
def main():
    """ main """
    d, n = [int(i) for i in input().split()]  # get input
    if d == 0:  # check if d is 0
        print(n)  # print n
    elif d == 1:  # check if d is 1
        print(100*n)  # print 100*n
    elif d == 2:  # check if d is 2
        print(10000*n)  # print 10000*n

if __name__ == "__main__":
    main()
