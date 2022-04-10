

# TODO:
# - This solution is not very efficient.
# - Need to find a better solution.

s = input()
t = input()

substring_length = 0

for i in range(len(s)):
    if s[i] in t:
        substring_length = 0
        if t == s[i:]:
            break
        else:
            t = t[1:]
    else:
        substring_length += 1

print(substring_length)