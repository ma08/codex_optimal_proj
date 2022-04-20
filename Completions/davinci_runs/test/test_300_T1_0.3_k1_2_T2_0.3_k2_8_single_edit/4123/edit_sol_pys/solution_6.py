

n = int(input())  # number of elements in the set
s = input()  # set

max_count = 0  # max count of two-grams
max_two_gram = ""  # max two-gram

for i in range(n-1):  # iterate through all possible two-grams
    two_gram = s[i:i+2]  # two-gram
    count = s.count(two_gram)  # count of two-grams
    if count > max_count:  # if the count of the two-gram is bigger than the max count,
        max_count = count  # then the max count is the count of the two-gram
        max_two_gram = two_gram  # and the max two-gram is the two-gram

print(max_two_gram)
