

n = int(input())

def check_odd(n):
    if n % 2 == 1:
        return True
    else:
        return False

def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

if n == 1:
    print("Either")
elif check_even(n):
    print("Even")
elif check_odd(n):
    print("Odd")
