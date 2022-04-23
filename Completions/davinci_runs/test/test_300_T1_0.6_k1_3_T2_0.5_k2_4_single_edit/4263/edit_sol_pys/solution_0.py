

s = input().strip()

# create a list of substrings of s that are only A, C, G, and T
acgt_strings = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        acgt_string = s[i:j]
        if acgt_string.count('A') > 0 and acgt_string.count('C') > 0 and acgt_string.count('G') > 0 and acgt_string.count('T') > 0:
            acgt_strings.append(acgt_string)

# print the length of the longest substring
print(max([len(acgt_string) for acgt_string in acgt_strings]))
