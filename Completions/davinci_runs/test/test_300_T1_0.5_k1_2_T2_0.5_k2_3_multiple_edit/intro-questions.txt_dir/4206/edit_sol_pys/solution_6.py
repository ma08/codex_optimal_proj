
import sys

def main():
    # read the input
    n = sys.stdin.readline()
    n = n.strip()
    n = int(n)
    #print(n)

    # convert n to a string
    n = str(n)
    #print(n)

    # split the string into a list of characters
    n = list(n)
    #print(n)

    # convert the list of characters to a list of integers
    n = list(map(int, n))
    #print(n)

    # sum the digits in n
    n = sum(n)
    #print(n)

    # if the sum is divisible by 3, n is divisible by 3 
    if n % 3 == 0:
        print(len(n) - 1)
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()
