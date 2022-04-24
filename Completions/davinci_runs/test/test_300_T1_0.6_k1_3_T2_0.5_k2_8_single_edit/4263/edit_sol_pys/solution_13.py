
s = input()

# create a list of substrings of s that are only A, C, G, and T,
# and store the length of the longest substring
max_length = 0
acgt_strings = []
for i in range(len(s)):
    for j in range(i, len(s)):
        if "A" in s[i:j+1] and "C" in s[i:j+1] and "G" in s[i:j+1] and "T" in s[i:j+1]:
            acgt_strings.append(s[i:j+1])
            if len(s[i:j+1]) > max_length:
                max_length = len(s[i:j+1])

# print the length of the longest substring
print(max_length)
