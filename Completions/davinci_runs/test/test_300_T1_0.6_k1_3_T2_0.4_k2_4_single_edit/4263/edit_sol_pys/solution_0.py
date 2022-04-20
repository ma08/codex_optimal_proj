

s = input("Enter a string: ")

# print the length of the longest substring of s that is only A, C, G, and T
print(max([len(s[i:j]) for i in range(len(s)) for j in range(i+1, len(s)+1) if "A" in s[i:j] and "C" in s[i:j] and "G" in s[i:j] and "T" in s[i:j]]))
