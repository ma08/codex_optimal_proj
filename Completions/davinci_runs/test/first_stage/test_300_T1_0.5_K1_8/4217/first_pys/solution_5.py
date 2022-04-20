

# get the inputs
n, m = map(int, input().split())

# create a list of lists that contains the foods the person likes
foods = []
for _ in range(n):
    foods.append(list(map(int, input().split())))

# remove the first element from each list
for i in range(n):
    foods[i].pop(0)

# get the foods that are liked by all the n people
common_foods = set(foods[0])
for i in range(1, n):
    common_foods = common_foods & set(foods[i])

# print the number of common foods
print(len(common_foods))