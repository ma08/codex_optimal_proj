

# The function is_lucky checks if a number is lucky, which means that it has exactly three different digits
def is_lucky(num):
    # Converts the number to a string and then to a list of numbers
    num = list(str(num))
    # Checks the length of the list of numbers, which is equal to the number of different digits
    if len(set(num)) == 3:
        return True
    else:
        return False

# Gets input from the user and converts it to an integer
num = int(input())

# Prints the result of the function is_lucky
print("Yes" if is_lucky(num) else "No")
