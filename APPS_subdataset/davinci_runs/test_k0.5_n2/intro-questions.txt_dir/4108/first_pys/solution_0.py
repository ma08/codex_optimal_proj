

# My answer
def equalize_strings(s, t):
    if s == t:
        return 'Yes'
    else:
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    s = s.replace(s[i], 'a')
                    s = s.replace(s[j], s[i])
                    s = s.replace('a', s[j])
                    if s == t:
                        return 'Yes'
        return 'No'

# A better answer
def equalize_strings(s, t):
    if (sorted(s) == sorted(t)):
        return 'Yes'
    else:
        return 'No'

# Test
s = input()
t = input()

print(equalize_strings(s, t))