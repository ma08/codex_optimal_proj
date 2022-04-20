

n = int(input())
a = list(map(int, input().split()))

# Create a list of the number of occurrences of each number in the list
# The length of this list is the number of pockets needed

occurrences = [0] * 101

for i in a:
    occurrences[i] += 1

count = 0

for i in range(1, 101):
    if occurrences[i] > 0:
        count += 1

print(count)