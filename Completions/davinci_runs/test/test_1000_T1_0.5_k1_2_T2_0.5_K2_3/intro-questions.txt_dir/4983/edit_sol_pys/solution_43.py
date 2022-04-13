
def main():
    x = int(input("Enter the number: "))
    while x > 9:
        digits = [int(d) for d in str(x)]
        product = 1
        for d in digits:
            if d != 0:
                product *= d
        x = product
    print("The answer is", x)

if __name__ == "__main__":
    main()
