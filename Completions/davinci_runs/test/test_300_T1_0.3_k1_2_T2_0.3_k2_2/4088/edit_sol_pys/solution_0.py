

def main():
    # read the number of test cases
    t = int(input())
    # iterate over test cases
    for i in range(t):
        # read the string
        s = input()
        # read the length of the array
        m = int(input())
        # read the array
        b = [int(x) for x in input().split()]
        # check if the length of the array is equal to the length of the string
        if len(b) != len(s):
            # if not, then print an error message
            print("ERROR!")
            # exit the program
            exit()
        # create an empty string
        t = ""
        # iterate over the string
        for j in range(len(s)):
            # iterate over the array
            for k in range(len(b)):
                # check if the value of the array is equal to zero
                if b[k] == 0:
                    # if so, then add the character to the string
                    t += s[k]
                # otherwise
                else:
                    # iterate over the string
                    for l in range(len(s)):
                        # check if the character of the string is greater than the character of the string
                        if ord(s[l]) > ord(s[k]):
                            # if so, then subtract the value of the array
                            b[k] -= abs(k - l)
                    # check if the value of the array is equal to zero
                    if b[k] == 0:
                        # if so, then add the character to the string
                        t += s[k]
        # print the string
        print(t)

if __name__ == "__main__":
    main()
