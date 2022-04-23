

s = input()

# create a list of substrings of s that are only A, C, G, and T
acgt_strings = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        acgt_string = s[i:j]
        if "A" in acgt_string and "C" in acgt_string and "G" in acgt_string and "T" in acgt_string and len(acgt_string) > 0:
            acgt_strings.append(acgt_string)

# print the length of the longest substring
print(max([len(acgt_string) for acgt_string in acgt_strings]))
