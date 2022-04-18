# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:14:27 2020


@author: mcsbi
"""

## Assignment: Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum and computing the product of 1,…,n.

n = int(input("Enter a number: "))

print("Do you want to find the sum or product of 1 to ", n, "?")

operation = input("Enter sum or product: ")

if operation == "sum":
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    print("The sum is: ", sum)
elif operation == "product":
    product = 1
    for i in range(1, n+1):
        product = product * i
    print("The product is: ", product)

## Assignment: Write a program that prints a multiplication table for numbers up to 12.

for i in range(1,13):
    for j in range(1,13):
        print(i*j, end = " ")
    print(" ")

## Assignment: Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)

for i in range(2,100):
    prime = True
    for j in range(2,i):
        if i % j == 0:
            prime = False
    if prime == True:
        print(i, end = " ")

## Assignment: Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

import random

secret_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

guess = int(input("Guess the number: "))

tries = 1

while guess != secret_number:
    if guess < secret_number:
        print("Too small!")
    elif guess > secret_number:
        print("Too large!")
    guess = int(input("Guess again: "))
    tries += 1

print("You got it! The number was ", secret_number)
print("And it only took you ", tries, "tries!")

## Assignment: Write a program that prints the next 20 leap years.

year = 2020

for i in range(1,21):
    if year % 4 == 0:
        print(year, end = " ")
    year += 1

## Assignment: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = input("Enter a digit: ")

x = int(a) + int(a*2) + int(a*3) + int(a*4)

print("The result is: ", x)

## Assignment: Write a program that computes the factorial of a given number.

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n+1):
    factorial = factorial * i

print("The factorial of ", n, "is: ", factorial)

## Assignment: Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)

for i in range(2,100):
    prime = True
    for j in range(2,i):
        if i % j == 0:
            prime = False
    if prime == True:
        print(i, end = " ")

## Assignment: Write a program that prints the next 20 leap years.

year = 2020

for i in range(1,21):
    if year % 4 == 0:
        print(year, end = " ")
    year += 1

## Assignment: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = input("Enter a digit: ")

x = int(a) + int(a*2) + int(a*3) + int(a*4)

print("The result is: ", x)

## Assignment: Write a program that computes the factorial of a given number.

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n+1):
    factorial = factorial * i

print("The factorial of ", n, "is: ", factorial)

## Assignment: Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

n = int(input("Enter a number: "))

sum = 0

for i in range(1, n+1):
    sum = sum + i

print("The sum of the numbers 1 to ", n, "is: ", sum)

## Assignment: Write a program that prints a multiplication table for numbers up to 12.

for i in range(1,13):
    for j in range(1,13):
        print(i*j, end = " ")
    print(" ")

## Assignment: Write a program that prints all prime numbers. (Note: if your programming language does not support arbitrary size numbers, printing all primes up to the largest number you can easily represent is fine too.)

for i in range(2,100):
    prime = True
    for j in range(2,i):
        if i % j == 0:
            prime = False
    if prime == True:
        print(i, end = " ")

## Assignment: Write a guessing game where the user has to guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

import random

secret_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

guess = int(input("Guess the number: "))

tries = 1

while guess != secret_number:
    if guess < secret_number:
        print("Too small!")
    elif guess > secret_number:
        print("Too large!")
    guess = int(input("Guess again: "))
    tries += 1

print("You got it! The number was ", secret_number)
print("And it only took you ", tries, "tries!")

## Assignment: Write a program that prints the next 20 leap years.

year = 2020

for i in range(1,21):
    if year % 4 == 0:
        print(year, end = " ")
    year += 1

## Assignment: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = input("Enter a digit: ")

x = int(a) + int(a*2) + int(a*3) + int(a*4)

print("The result is: ", x)

## Assignment: Write a program that computes the factorial of
