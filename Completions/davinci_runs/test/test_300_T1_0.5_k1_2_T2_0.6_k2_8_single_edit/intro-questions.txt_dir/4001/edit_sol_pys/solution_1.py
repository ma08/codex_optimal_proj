
# read N
N = int(input())
# read list
L = input().split()

# create dictionary for numbers
D = {i: L.count(i) for i in L}

# print numbers
print(D)
