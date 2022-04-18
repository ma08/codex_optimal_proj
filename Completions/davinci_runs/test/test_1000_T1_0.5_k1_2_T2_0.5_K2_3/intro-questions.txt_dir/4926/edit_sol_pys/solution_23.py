# Solution:


def factorial(x):  # define function
    if x == 0:  # if x is zero
        return 1  # return 1
    else:  # otherwise
        return x * factorial(x - 1)  # return x multiplied by factorial of x-1


def e_approx(n):
    approx = 0  # define variable
    for i in range(n + 1):  # for each number from 0 to n
        approx += 1 / factorial(i)  # add 1 over factorial(i) to approx
    return approx  # return approx


def main():
    n = int(input())  # define n
    print(e_approx(n))  # print e_approx(n)


main()
