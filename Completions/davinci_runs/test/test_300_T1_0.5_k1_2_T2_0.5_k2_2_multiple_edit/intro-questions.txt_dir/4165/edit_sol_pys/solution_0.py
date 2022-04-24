
n = int(input("Enter the number of elements: "))
l = list(map(int, input("Enter the elements: ").split()))

if max(l) < sum(l) - max(l):
    print("Yes")
else:
    print("No")
