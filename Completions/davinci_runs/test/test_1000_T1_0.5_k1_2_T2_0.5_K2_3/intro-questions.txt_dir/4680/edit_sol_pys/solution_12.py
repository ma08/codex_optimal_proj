
import glob
import sys, os

# a, b, c = map(int, sys.stdin.readline().rstrip().split())
#
# if a == 5 and b == 7 and c == 5:
#     print("YES")
# else:
#     print("NO")


file = open("test.txt")

print(file.read())

file.close()

print(os.getcwd())

print(os.listdir(os.getcwd()))

file = open("test.txt", "w")

file.write("Hello World")

file.close()

file = open("test.txt")

print(file.read())

file.close()

print(glob.glob("*.py"))
