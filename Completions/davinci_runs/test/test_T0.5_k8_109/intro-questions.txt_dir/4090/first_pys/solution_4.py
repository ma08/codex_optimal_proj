

n = int(input())
w = input().split()

# create a list of the unique words
unique = []

for word in w:
    if word not in unique:
        unique.append(word)

# create a dictionary of the number of times each word appears
count = {}

for word in unique:
    count[word] = 0

for word in w:
    count[word] += 1

# create a list of the number of times each word appears
num = []

for word in unique:
    num.append(count[word])

# create a list of the lengths of the words
lengths = []

for word in unique:
    lengths.append(len(word))

# create a list of the lengths of the words multiplied by the number of times each word appears
product = []

for i in range(len(unique)):
    product.append(lengths[i] * num[i])

# create a list of the lengths of the words multiplied by the number of times each word appears minus the number of times each word appears
difference = []

for i in range(len(unique)):
    difference.append(product[i] - num[i])

# sum the list of the lengths of the words multiplied by the number of times each word appears minus the number of times each word appears
sum_difference = sum(difference)

# if the sum is less than the number of words in the text, then the length of the text after at most one abbreviation is the sum of the lengths of the words
if sum_difference < n:
    print(sum_difference)
# if the sum is greater than or equal to the number of words in the text, then the length of the text after at most one abbreviation is the number of words in the text
else:
    print(n)