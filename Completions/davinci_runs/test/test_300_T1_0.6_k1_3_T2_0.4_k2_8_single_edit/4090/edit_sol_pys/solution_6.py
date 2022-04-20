
n = int(input())
words = input().split()

# Find all the words that are repeated in the list
repeats = set()
for word in words:
    if words.count(word) > 1:
        repeats.add(word)

# Find the length of the text before abbreviation
length_before = len(" ".join(words))

# Find the length of the text after abbreviating the list 
length_after = length_before
for repeat in repeats:
    # Find all the indices of a word
    indices = [i for i, word in enumerate(words) if word == repeat]
    # Find the length of the text after abbreviating the first occurrence of the word
    length_after = min(length_after, length_before - (len(repeat) - 1) * len(indices) + len(indices) - 1)
    # Find the length of the text after abbreviating the second occurrence of the word
    if len(indices) > 1:
        length_after = min(length_after, length_before - (len(repeat) - 1) * (len(indices) - 1) + len(indices) - 2)

print(length_after)
