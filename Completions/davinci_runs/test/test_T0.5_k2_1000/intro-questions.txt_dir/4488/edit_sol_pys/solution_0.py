
import sys

def main():
    num1 = sys.stdin.readline().rstrip() # readline() reads a line from the file; rstrip() removes any trailing characters (default space)
    num2 = sys.stdin.readline().rstrip() # readline() reads a line from the file; rstrip() removes any trailing characters (default space)

    if len(num1) > len(num2): # if the length of num1 is greater than the length of num2
        print("GREATER")
    elif len(num1) < len(num2): # if the length of num1 is less than the length of num2
        print("LESS")
    else:
        for i in range(len(num1)): # for each index in the range of the length of num1
            if int(num1[i]) > int(num2[i]): # if the integer value of num1 at index i is greater than the integer value of num2 at index i
                print("GREATER")
                break
            elif int(num1[i]) < int(num2[i]): # if the integer value of num1 at index i is less than the integer value of num2 at index i
                print("LESS")
                break
            else: # if the integer value of num1 at index i is equal to the integer value of num2 at index i
                if i == len(num1)-1: # if i is equal to the length of num1 minus one
                    print("EQUAL")

if __name__ == '__main__':
    main()
