

s = input()

# create a list of substrings of s that are only A, C, G, and T
acgt_strings = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        substring = s[i:j]
        if "A" in substring and "C" in substring and "G" in substring and "T" in substring:
            acgt_strings.append(substring)

# print the length of the longest substring
print(max([len(substring) for substring in acgt_strings]))
