

n = int(input("Enter the number of elements:"))

arr = []
for i in range(n):
    ele = int(input("Enter the element:"))
    arr.append(ele)

arr.sort()
print(arr)
