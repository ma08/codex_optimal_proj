import sys

def main():
    num1 = sys.stdin.readline().rstrip() # read the first line
    num2 = sys.stdin.readline().rstrip() # read the second line

    if len(num1) > len(num2):
        print("GREATER")
    elif len(num1) < len(num2):
        print("LESS")
    else:
        for i in range(len(num1)): # iterate through the numbers
            if int(num1[i]) > int(num2[i]): # if the first number is greater, print GREATER
                print("GREATER")
                break
            elif int(num1[i]) < int(num2[i]): # if the first number is less, print LESS
                print("LESS")
                break
            else:
                if i == len(num1)-1: # if the numbers are equal, print EQUAL
                    print("EQUAL")

if __name__ == '__main__':
    main()
