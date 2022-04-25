# Hello world

k = int(input("Enter a number: "))
s = input("Enter a string: ")

if len(s) <= k:
    print(s)
else:
    print(s[:k] + "...")
