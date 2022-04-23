
n = int(input())
words = input().split()

repeats = set()
for word in words:
    if words.count(word) > 1:
        repeats.add(word)

length_before = len(" ".join(words))

length_after = length_before
for repeat in repeats:
    indices = [i for i, word in enumerate(words) if word == repeat]
    length_after = min(length_after, length_before - (len(repeat) - 1) * len(indices) + len(indices) - 1)
    if len(indices) > 1:
        length_after = min(length_after, length_before - (len(repeat) - 1) * (len(indices) - 1) + len(indices) - 2)

print(length_after)
