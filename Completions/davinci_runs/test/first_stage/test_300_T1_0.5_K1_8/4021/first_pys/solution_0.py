

# define the main function
def main():
    # get the input from the user
    a = int(input())
    
    # initialize the variables
    i = 1
    j = 1
    k = 1
    
    # create a while loop to find the answer
    while True:
        # check if the sum of i, j, and k is equal to a
        if (i + j + k) == a:
            print(k)
            break
        # check if the sum of i, j, and k is greater than a
        elif (i + j + k) > a:
            # increment i
            i += 1
            # reset j and k
            j = i
            k = i
        # check if the sum of i, j, and k is less than a
        elif (i + j + k) < a:
            # increment j
            j += 1
            # check if the sum of i, j, and k is equal to a
            if (i + j + k) == a:
                print(k)
                break
            # check if the sum of i, j, and k is greater than a
            elif (i + j + k) > a:
                # increment i
                i += 1
                # reset j and k
                j = i
                k = i
            # check if the sum of i, j, and k is less than a
            elif (i + j + k) < a:
                # increment k
                k += 1
                # check if the sum of i, j, and k is equal to a
                if (i + j + k) == a:
                    print(k)
                    break
                # check if the sum of i, j, and k is greater than a
                elif (i + j + k) > a:
                    # increment i
                    i += 1
                    # reset j and k
                    j = i
                    k = i

# call the main function
main()