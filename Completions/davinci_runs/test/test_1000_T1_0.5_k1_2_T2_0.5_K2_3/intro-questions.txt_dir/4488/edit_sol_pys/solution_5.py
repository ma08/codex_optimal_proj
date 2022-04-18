import sys

def main():
    num1 = sys.stdin.readline().rstrip() #readline() reads a single line from the file
    num2 = sys.stdin.readline().rstrip() #rstrip() removes all the trailing whitespaces and newline characters

    if len(num1) > len(num2):
        print("GREATER")
    elif len(num1) < len(num2):
        print("LESS")
    else:
        for i in range(len(num1)):
            if int(num1[i]) > int(num2[i]): #int() converts string to integer
                print("GREATER")
                break
            elif int(num1[i]) < int(num2[i]):
                print("LESS")
                break
            else:
                if i == len(num1)-1:
                    print("EQUAL")

if __name__ == '__main__':
    main()
