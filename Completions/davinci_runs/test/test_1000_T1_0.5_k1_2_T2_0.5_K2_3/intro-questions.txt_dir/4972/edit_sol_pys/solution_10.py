
def main():
    """main function"""
    x = int(input("Enter a number: "))
    k = 0
    while x > 1:
        k += 1
        x = x // (2 * k + 1)
    print("The number of times the operation is performed is: ", k)

if __name__ == "__main__":
    main()
