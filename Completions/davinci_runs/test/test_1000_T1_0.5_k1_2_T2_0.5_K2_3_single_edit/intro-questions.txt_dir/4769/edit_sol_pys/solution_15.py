

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

word = raw_input()

for i in range(len(word) - 1):
    for j in range(i + 1, len(word)):
        if is_anagram(word[:i], word[i:j]):
            print word[:i]
            exit()

print -1
