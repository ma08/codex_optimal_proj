

n = int(input("Enter the number of elements in the array: "))
a = input("Enter the elements of the array: ").split()

for i in range(n):
    if a[i] != "mumble" and int(a[i]) != i+1:
        print("Something is fishy")
        exit()

print("makes sense")
