

#inputs
n = int(input())
a = [int(x) for x in input().split()]

#create a list of the number of occurrences of each value
counts = [0] * 101
for i in range(n):
    counts[a[i]] += 1

#count the number of different values
num_different = 0
for i in range(1, 101):
    if counts[i] != 0:
        num_different += 1

#print the answer
print(num_different)