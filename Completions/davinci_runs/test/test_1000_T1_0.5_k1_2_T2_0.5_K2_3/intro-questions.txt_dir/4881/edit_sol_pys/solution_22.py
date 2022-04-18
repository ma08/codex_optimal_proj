
n = int(input()) # input

def check_odd(n):
    return n % 2 == 1


def check_even(n):
    return n % 2 == 0


if n == 1:
    print("Either")
elif n % 2 == 0:
    print("Even")
else:
    print("Odd")
