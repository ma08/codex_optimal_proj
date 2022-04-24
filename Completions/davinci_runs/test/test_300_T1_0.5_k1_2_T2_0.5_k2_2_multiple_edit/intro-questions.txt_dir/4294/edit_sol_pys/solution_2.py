

def main():
    # Write a program that outputs the string representation of numbers from 1 to n.
    # But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
    # For numbers which are multiples of both three and five output “FizzBuzz”.
    n = int(input())

    # Write your code here
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == '__main__':
    main()
