
# This problem is solved by using the count() method
# count() takes in a string and returns the number of times the string is found

# Gets input
s = input()
n = int(input())

# Gets the number of times 'a' appears in the string
print(s.count('a') * (n // len(s)) + s[:n % len(s)].count('a'))
