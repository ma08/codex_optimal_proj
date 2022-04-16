
import sys

def factorial(n):
    if n == 1:
        return 1
    else:
        return (n * factorial(n-1)) % 10

def main():
    for i in range(int(input())):
        print(factorial(int(input())))

main()
