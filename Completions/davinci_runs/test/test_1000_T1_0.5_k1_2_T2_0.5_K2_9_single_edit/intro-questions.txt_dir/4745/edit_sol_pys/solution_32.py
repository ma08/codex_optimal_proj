


n, X = map(int, input().split())
prices = list(map(int, input().split()))

# sort the prices and keep track of the original index
prices_with_indices = list(enumerate(prices))
prices_with_indices.sort(key = lambda x: x[1])

# create a list of all indices
indices = [x[0] for x in prices_with_indices]

# create a list of all prices
prices = [x[1] for x in prices_with_indices]

# create a list of all possible pairs of prices
pairs = [(prices[i], prices[j]) for i in range(len(prices)) for j in range(i+1, len(prices))]

# filter out all pairs with sum less than X
pairs = list(filter(lambda x: x[0] + x[1] > X, pairs))

# sort the pairs by the first entry in descending order
pairs.sort(key = lambda x: x[0], reverse = True)

# create a set of all used indices
used_indices = set()

# go through all pairs
for pair in pairs:
    # if the first index is not used, add it to the used indices
    if indices[prices.index(pair[0])] not in used_indices:
        used_indices.add(indices[prices.index(pair[0])])
    # if the second index is not used, add it to the used indices
    if indices[prices.index(pair[1])] not in used_indices:
        used_indices.add(indices[prices.index(pair[1])])

print(len(used_indices))
