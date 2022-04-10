

n = int(input())
s = input()

# Find the first character which is not equal to the last character
# If we replace all characters with the last character, we will get a balanced string
# If we replace it with the character right after the last character, we will get a lexicographically smaller string
i = 0
while s[i] == s[-1]:
    i += 1

print(s[:i] + s[-1] * (n - i) if s[i] == s[-2] else s[:i] + s[-2] + s[-1] * (n - i - 1))