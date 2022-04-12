#!/usr/bin/python3

n = int(input("Enter the number of elements: "))
a = input("Enter the elements: ").split()

for i in range(n):
    if a[i] != "mumble" and int(a[i]) != i+1:
        print("something is fishy")
        exit()

print("makes sense")
