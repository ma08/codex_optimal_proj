

def main():
    # read the number of test cases
    t = int(input())
    # iterate over test cases
    for i in range(t):
        # read the length of the array
        m = int(input())
        # read the array
        b = [int(x) for x in input().split()]
        # create an empty string
        t = ""
        # iterate over the array
        for j in range(len(b)):
            # check if the value of the array is equal to zero
            if b[j] == 0:
                # if so, then add the character to the string and remove the character from the array
                t += chr(b[j])
                b.remove(b[j])
            # otherwise
            else:
                # iterate over the array
                for k in range(len(b)):
                    # check if the value of the array is greater than the value of the array
                    if b[k] > b[j]:
                        # if so, then subtract the value of the array
                        b[j] -= abs(b[j] - b[k])
                # check if the value of the array is equal to zero
                if b[j] == 0:
                    # if so, then add the character to the string and remove the character from the array
                    t += chr(b[j])
                    b.remove(b[j])
        # print the string
        print(t)

if __name__ == "__main__":
    main()
