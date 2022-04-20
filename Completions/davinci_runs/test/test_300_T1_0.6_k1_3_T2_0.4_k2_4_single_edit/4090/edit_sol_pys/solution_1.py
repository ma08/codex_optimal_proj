

n = int(input())  # number of words
words = input().split()  # words

# Find all the words that are repeated in the list of words
repeats = set()
for word in words:
    if words.count(word) > 1:
        repeats.add(word)

# Find the length of the text before abbreviation (in characters)
length_before = len(" ".join(words))

# Find the length of the text after abbreviating the list of words
length_after = length_before
for repeat in repeats:
    # Find all the indices of a repeated word
    indices = [i for i, word in enumerate(words) if word == repeat]
    # Find the length of the text after abbreviating the first occurrence of the repeated word
    length_after = min(length_after, length_before - (len(repeat) - 1) * len(indices) + len(indices) - 1)
    # Find the length of the text after abbreviating the second occurrence of the repeated word
    if len(indices) > 1:
        length_after = min(length_after, length_before - (len(repeat) - 1) * (len(indices) - 1) + len(indices) - 2)

print(length_after)
