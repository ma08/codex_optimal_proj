n, c = map(int, input().split())
fruits = list(map(int, input().split()))

# create a set of unique fruits.
unique_fruits = set()

# iterate over the fruits.
for fruit in fruits:
    # if the fruit is not in the set and we have enough capacity.
    # add the fruit to the set.
    if fruit not in unique_fruits and c - fruit >= 0:
        unique_fruits.add(fruit)
        c -= fruit

# print the number of unique fruits
print(len(unique_fruits))
