
#
# Getting input
a = int(input())

#
# Defining function for checking if a number is interesting
def is_interesting(n):
    """
    Returns true if number is interesting else returns false.
    """
    return int(sum(list(map(int, list(str(n))))) % 4) == 0

#
# Finding the nearest interesting number
n = a
#
while not is_interesting(n):
    n += 1

# Printing the answer
print(n)
