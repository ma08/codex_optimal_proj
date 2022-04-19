

def main():
    # read the number of test cases
    t = int(input())
    # iterate over test cases
    for i in range(t):
        # read the length of the array
        m = int(input())
        # read the array
        # read the string
        s = input()
        b = [int(x) for x in input().split()]
        # check if the length of the array is equal to the length of the string
        if len(b) != len(s):
            print("ERROR!") # print an error message
            exit() # exit the program
        # create an empty string
        t = ""
        # iterate over the array
        for j in range(len(b)):
            # check if the value of the array is equal to zero
            if b[j] == 0:
                # if so, then add the character to the string
                t += s[j]
            # otherwise
            else:
                # iterate over the string
                for k in range(len(s)):
                    # check if the character of the string is greater than the character of the string
                    if ord(s[k]) > ord(s[j]):
                        # if so, then subtract the value of the array
                        b[j] -= abs(j - k)
                # check if the value of the array is equal to zero
                if b[j] == 0:
                    # if so, then add the character to the string
                    t += s[j]
        # print the string
        print(t)

if __name__ == "__main__":
    main()
