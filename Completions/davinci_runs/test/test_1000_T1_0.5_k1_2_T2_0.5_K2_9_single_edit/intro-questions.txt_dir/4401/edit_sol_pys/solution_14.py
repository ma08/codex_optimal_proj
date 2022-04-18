# Write a program that reads a file and prints what you wrote three times.
# This time, use the with statement.


with open("file.txt", "w") as f:
    f.write("I love programming.\n")
    f.write("I love programming.\n")
    f.write("I love programming.\n")

with open("file.txt", "r") as f:
    print(f.read())
