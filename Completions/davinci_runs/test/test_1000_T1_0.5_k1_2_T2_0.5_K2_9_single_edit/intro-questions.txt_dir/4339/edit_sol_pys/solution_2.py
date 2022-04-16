

# -----Solution-----

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Sort the a and b lists in descending order
a.sort()
b.sort()

# Initialize the sum to 0
sum = 0

i = len(a)
j = len(b)

# Iterate through the two lists in descending order
while i > 0 and j > 0:
    # If the sum of the two values is greater than the sum of the two values in the other list, increase the sum by the sum of the two values
    if a[i] + b[j] > a[i] + b[j]:
        sum += a[i] + b[j]
        i -= 1
        j -= 1
    # Otherwise, increase the index of the second list, and add the value of the second list to the sum
    elif a[i] + b[j] < a[i] + b[j]:
        sum += a[i] + b[j]
        j -= 1
    # If the two values are equal, add the value of the first list to the sum, and decrease the index of the second list
    else:
        sum += a[i]
        j -= 1

print(sum)
