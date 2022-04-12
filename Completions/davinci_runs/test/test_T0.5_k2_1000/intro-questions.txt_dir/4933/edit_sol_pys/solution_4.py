

def main():
    """main function"""
    num = list(map(int, input().split())) # input
    num.sort() # sort
    if num[1] - num[0] == num[2] - num[1]: # check if it is arithmetic
        print(num[2] + num[1] - num[0]) # print
    else: # if not
        print(num[1] + num[2] - num[0]) # print

main()
