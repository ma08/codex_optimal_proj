import math


def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, math.ceil(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        if prime(x):
            print("Prime")
        else:
            print("Not Prime")

if __name__ == "__main__":
    main()
