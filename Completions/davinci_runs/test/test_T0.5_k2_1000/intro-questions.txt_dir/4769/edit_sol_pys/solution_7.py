
def is_anagram(s, t): # check if two strings are anagrams
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

word = raw_input() # input word

for i in range(len(word)): # iterate through the word
    for j in range(i, len(word)): # iterate through the word
        if is_anagram(word[:i], word[i:j+1]): # check if the two parts are anagrams
            print word[:i] # print the first part
            exit()

print -1
