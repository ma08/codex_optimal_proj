

def main():
    n, x, y = [int(x) for x in input().split()]
    number = input()
    result = int(number, 2)
    #print(result)
    rem = result % (10 ** x)
    #print(rem)
    if rem == 10 ** y:
        print(0)
    else:
        #print(rem)
        rem = 10 ** y - rem
        #print(rem)
        if rem % 2 == 0:
            print(1)
        else:
            print(2)

if __name__ == "__main__":
    main()