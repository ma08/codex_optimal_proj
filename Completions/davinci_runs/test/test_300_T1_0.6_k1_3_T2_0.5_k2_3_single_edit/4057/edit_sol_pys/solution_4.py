
n = int(input("Enter the number of elements in the array: "))
a = []
for i in range(n):
    a.append(int(input("Enter the next element: ")))
print("The number of distinct elements is: ", len(set(a)))
