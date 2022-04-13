

n = input()
n = int(n)

def is_odd(n):
    return n % 2 == 1

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

if n == 1:
    print("Either")
elif n % 2 == 0:
    print("Even")
else:
    print("Odd")
