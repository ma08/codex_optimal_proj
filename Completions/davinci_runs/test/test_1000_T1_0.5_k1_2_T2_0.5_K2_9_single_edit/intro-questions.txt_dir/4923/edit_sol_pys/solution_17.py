def main():
    n = int(input("Enter the number of integers: "))
    numbers = list(map(int, input("Enter the numbers: ").split()))
    print("The largest number is {}".format(max(numbers)))



if __name__ == "__main__":
    main()
