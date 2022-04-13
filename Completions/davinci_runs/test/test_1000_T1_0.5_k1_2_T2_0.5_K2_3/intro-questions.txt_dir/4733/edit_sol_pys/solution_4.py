import sys
import math

# open file in read mode
def main():
    # iterate through each line
    test_cases = open(sys.argv[1], 'r')
    # strip and split line
    for test in test_cases:
    # get number of nodes
        test = test.strip().split()
    # get in or out
        n = int(test[0])
    # if the number of nodes is even
        s = test[1]
    # if the tree is out
        if n % 2 == 0:
        # print log base 2 of the number of nodes
            if s == "out":
                print(math.log(n, 2))
        # else print log base 2 of the number of nodes + 1
            else:
                print(math.log(n, 2) + 1)
    # else if the number of nodes is odd
        else:
        # if the tree is out
            if s == "out":
            # print log base 2 of the number of nodes + 1
                print(math.log(n, 2) + 1)
            else:
            # else print log base 2 of the number of nodes
                print(math.log(n, 2))
    # close file
    test_cases.close()

# call main
main()
