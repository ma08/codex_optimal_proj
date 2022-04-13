

def main():
    """main function"""
    num = int(input()) # take the input
    k = 0 # counter
    while num > 1: # while loop
        k += 1 # increment
        num = num // (2*k + 1) # divide
    print(k) # print

if __name__ == "__main__":
    main()
