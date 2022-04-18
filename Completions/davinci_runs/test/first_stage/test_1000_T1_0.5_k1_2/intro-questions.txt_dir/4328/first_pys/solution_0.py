

#-----main function-----

def main():
    #get input
    A, B = map(int, input().split())

    #check if A is a divisor of B
    if B % A == 0:
        print(A + B)
    else:
        print(B - A)

if __name__ == '__main__':
    main()