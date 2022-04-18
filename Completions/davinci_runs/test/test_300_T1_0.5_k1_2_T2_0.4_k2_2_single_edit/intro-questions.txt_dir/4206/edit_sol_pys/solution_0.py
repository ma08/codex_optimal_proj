
import sys

def main():
    # read the input
    input_string = sys.stdin.readline()
    input_string = input_string.strip()
    input_string = int(input_string)
    #print(input_string)

    # convert s to a string
    input_string = str(input_string)
    #print(input_string)

    # split the string into a list of characters
    input_string = list(input_string)
    #print(input_string)

    # convert the list of characters to a list of integers
    input_string = list(map(int, input_string))
    #print(input_string)

    # sum the digits in s
    input_string = sum(input_string)
    #print(input_string)

    # if the sum is divisible by 3, s is divisible by 3
    if input_string % 3 == 0:
        print(len(input_string) - 1)
    else:
        print(0)

    return 0

if __name__ == "__main__":
    main()
