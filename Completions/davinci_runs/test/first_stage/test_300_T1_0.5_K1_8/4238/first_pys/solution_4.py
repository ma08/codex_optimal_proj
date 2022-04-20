

# N is an integer, so we can use the remainder operator to determine if
# it is a multiple of 9.

def is_multiple_of_9(n):
    if n % 9 == 0:
        return True
    else:
        return False

n = int(input())

if is_multiple_of_9(n):
    print("Yes")
else:
    print("No")