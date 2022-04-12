

def main():
    k = int(input("Enter the number of terms: ")) # get the number of terms
    a, b = 0, 1
    for i in range(k): # loop for the number of terms
        a, b = b, a+b
    print(a, b) # print the results

if __name__ == "__main__":
    main()
