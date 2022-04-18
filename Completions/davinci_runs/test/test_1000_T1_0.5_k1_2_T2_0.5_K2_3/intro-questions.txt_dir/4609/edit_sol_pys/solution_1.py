n = int(input("Enter the number of elements in the list"))
l = [int(input()) for _ in range(n)]
l = set(l)
print(len(l))
