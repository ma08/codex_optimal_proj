

n = int(input("Enter number of elements : "))
a = [int(x) for x in input("Enter elements : ").split()]

people_disturbed = 0

for i in range(1, n - 1):
    if a[i - 1] == a[i + 1] == 1 and a[i] == 0:
        people_disturbed += 1

print(people_disturbed)
