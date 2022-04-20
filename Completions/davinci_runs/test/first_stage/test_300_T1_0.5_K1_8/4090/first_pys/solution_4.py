

# SOLUTION
# First, we calculate the number of occurrences for each word.
# Then, we find the maximum number of occurrences for any word.
# Finally, we calculate the total number of letters in the text,
# and subtract the number of occurrences of the most frequent word.
# We add 1 because we also need to count the number of spaces.

n = int(input())
words = input().split()

occurrences = {}
for word in words:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1

max_occurrences = max(occurrences.values())

total_letters = sum(len(word) for word in words)

print(total_letters - max_occurrences + 1)