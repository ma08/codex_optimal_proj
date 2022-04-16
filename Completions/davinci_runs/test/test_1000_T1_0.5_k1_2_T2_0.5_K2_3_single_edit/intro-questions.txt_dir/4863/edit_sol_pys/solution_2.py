# Python program to count the number of occurences of a character in a string
# using recursion

n = int(input())
a = input()
score = 0


def countOccurences(str, n):
    if (n == 0):
        return 0
    if (str[n - 1] == 'A'):
        return 1 + countOccurences(str, n - 1)
    else:
        return 0 + countOccurences(str, n - 1)


print(countOccurences(a, n))
