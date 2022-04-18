

#-----main function-----

def main():
    #get input and convert to int
    a, b = map(int, input().split())

    #check if A is a divisor of B.
    if b % a == 0:
        print(a + b)
    else:
        print(b - a)

if __name__ == '__main__':
    main()
