

s = input()

# create a list of substrings of s that are only A, C, G, and T and have length >= 5
acgt_strings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if "A" in s[i:j] and "C" in s[i:j] and "G" in s[i:j] and "T" in s[i:j] and len(s[i:j]) >= 5]

# print the length of the longest substring
print(max([len(acgt_string) for acgt_string in acgt_strings]) if acgt_strings else 0)
