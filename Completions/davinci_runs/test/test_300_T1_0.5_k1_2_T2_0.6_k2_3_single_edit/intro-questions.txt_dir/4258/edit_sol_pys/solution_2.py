#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Sept 2019
# This is program loops a number


def main():
    # funciton adds numbers

    # variable
    answer = 0

    # input
    integer = int(input("What is your number: "))

    # process & output
    for repeater in range(integer + 1):
        answer = answer + repeater
        print(repeater)

    print("The sum of your number is: {}"
          .format(answer))


if __name__ == "__main__":
    main()
