
# Read input
n = int(input())
a = list(map(int, input().split()))
unique_numbers = set(a)
if len(unique_numbers) == 1:
    print("none")
else:
    for i in range(6, 0, -1):
        if i in unique_numbers:
            highest_unique = i
            break
    for i in range(n):
        if a[i] == highest_unique:
            print(i + 1)
            break
