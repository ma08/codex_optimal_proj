

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

word = input()

for i in range(1, len(word)):
    if is_anagram(word[:i], word[i:]):
        print(word[:i])
        exit()

print -1
