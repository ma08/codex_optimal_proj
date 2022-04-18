

s = input()

# create a list of substrings of s that are only A, C, G, and T and print the length of the longest substring
print(max([len(acgt_string) for acgt_string in [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1) if "A" in s[i:j] and "C" in s[i:j] and "G" in s[i:j] and "T" in s[i:j]]]))
