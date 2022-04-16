
n, c = map(int, input().split())
fruits = list(map(int, input().split()))

# create a set of unique fruits
unique_fruits = set()

# iterate over the fruits and add unique fruits to the set
for fruit in fruits:
    if fruit not in unique_fruits and c - fruit >= 0:
        unique_fruits.add(fruit)
        c -= fruit

# print the number of unique fruits
print(len(unique_fruits))
