

# Get input and convert to integer
n = int(input("Enter number of elements : "))
a = list(map(int, input("\nEnter the numbers : ").split()))

# Check if the number is even
for i in range(n):
    if a[i] % 2 == 0:
        print("\nThe number is even")
        break
else:
    print("\nThe number is odd")
