
def main():
    x = float(input("Enter a fraction: "))

    for i in range(1, 10):

        for j in range(1, 10):
            if i / j == x:  # check if the fraction is equal to the input
                print(i, j)  # print the numerator and denominator
                break

if __name__ == '__main__':
    main()
