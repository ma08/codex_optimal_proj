

# Check if the number is divisible by 3 or not
def isDivisibleBy3(number):
    return number % 3 == 0;


# Check if the number is divisible by 5 or not
def isDivisibleBy5(number):
    return number % 5 == 0;


# Get the sum of digits
def getSumOfDigits(number):
    sum = 0;
    while number != 0:
        sum += number % 10;
        number //= 10;
    return sum;


def main():
    # Get the input
    number = int(input());

    # Check if divisible by 3 or 5
    if isDivisibleBy3(number) or isDivisibleBy5(number):
        print("Yes");
    else:
        # Check if the sum of digits is divisible by 3 or 5
        if isDivisibleBy3(getSumOfDigits(number)) or isDivisibleBy5(getSumOfDigits(number)):
            print("Yes");
        else:
            print("No");


if __name__ == '__main__':
    main();
