# Chess pieces.

pieces = [1, 1, 2, 2, 2, 8]
count = [int(i) for i in input().split()]

for i in range(6):
    print(pieces[i] - count[i], end=" ")
