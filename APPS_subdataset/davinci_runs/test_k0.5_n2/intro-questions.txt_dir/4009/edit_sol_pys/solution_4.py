

def main():
    n, x, y = [int(x) for x in input().split()] # get input
    number = input()
    result = int(number, 2) # convert to decimal
    # print(result)
    rem = result % (10 ** x) # get remainder
    # print(rem)
    if rem == 10 ** y: # check if remainder is equal to 10^y
        print(0)
    else:
        # print(rem)
        rem = 10 ** y - rem # subtract remainder from 10^y
        # print(rem)
        if rem % 2 == 0: # check if remainder is even
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()
