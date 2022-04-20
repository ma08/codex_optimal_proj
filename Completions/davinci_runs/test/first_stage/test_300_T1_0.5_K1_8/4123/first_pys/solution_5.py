

n = int(input())
s = input()

# create a list of tuples containing each two-gram and the number of times it appears in the string
two_grams = [(s[i:i+2], s.count(s[i:i+2])) for i in range(n-1)]

# find the maximum number of times a two-gram appears in the string
max_count = max([i[1] for i in two_grams])

# find the two-gram that appears the most
for i in two_grams:
    if i[1] == max_count:
        print(i[0])
        break