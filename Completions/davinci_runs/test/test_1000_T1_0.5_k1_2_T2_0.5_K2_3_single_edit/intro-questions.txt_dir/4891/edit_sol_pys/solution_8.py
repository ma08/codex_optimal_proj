
pieces = [1, 1, 2, 2, 2, 8]
count = [int(i) for i in input().split()]  # read list of integers
# print(count)

for i in range(6):
    print(pieces[i] - count[i], end=" ")  # print difference of lists

# print(pieces[0])
