
n, c = [int(x) for x in input().split()]
fruits = [int(x) for x in input().split()]

unique_fruits = set()

for fruit in fruits:
    if fruit not in unique_fruits and c - fruit >= 0:
        unique_fruits.add(fruit)
        c -= fruit

print(len(unique_fruits))
