

# WORKS (TESTED) - 1

[n, c] = [int(i) for i in input().split()]
seq = [int(i) for i in input().split()]

freq_dict = {}

for i in range(c+1):
    freq_dict[i] = 0

for i in seq:
    freq_dict[i] += 1

new_seq = []

for key in freq_dict:
    if freq_dict[key] != 0:
        new_seq.extend([key]*freq_dict[key])

print(" ".join([str(i) for i in new_seq]))

####################################################################################

# WORKS (TESTED) - 2

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort()

print(" ".join([str(i) for i in arr]))

####################################################################################

# WORKS (TESTED) - 3

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort(reverse=True)

print(" ".join([str(i) for i in arr]))

####################################################################################

# WORKS (TESTED) - 4

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort()

for i in range(n):
    print(arr[i], end=" ")

####################################################################################

# WORKS (TESTED) - 5

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort(reverse=True)

for i in range(n):
    print(arr[i], end=" ")

####################################################################################

# WORKS (TESTED) - 6

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort()

for i in range(n):
    print(arr[i])

####################################################################################

# WORKS (TESTED) - 7

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort(reverse=True)

for i in range(n):
    print(arr[i])

####################################################################################

# WORKS (TESTED) - 8

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort()

for i in range(n):
    print(arr[i], end=" ")

print()

####################################################################################

# WORKS (TESTED) - 9

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort(reverse=True)

for i in range(n):
    print(arr[i], end=" ")

print()

####################################################################################

# WORKS (TESTED) - 10

n = int(input())

arr = [int(i) for i in input().split()]

arr.sort()

for i in range(n):
    print(arr[i])

print()

####################################################################################
