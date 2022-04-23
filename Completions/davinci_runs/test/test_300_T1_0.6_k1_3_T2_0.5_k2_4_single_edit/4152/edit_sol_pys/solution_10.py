#!/usr/bin/env python3

# Created by: Evano Fotia
# Created on: oct 2019
# This program can write to a file

import csv


def main():
    # this function can write to a file

    # input
    number_as_string = input("Enter a number: ")
    number_as_number = int(number_as_string)

    # process
    if number_as_number == 1:
        print("")
        print("You entered:", number_as_number)
        print("")

    # output
    with open("number.txt", "w") as file_object:
        file_object.write(number_as_string)


if __name__ == "__main__":
    main()
