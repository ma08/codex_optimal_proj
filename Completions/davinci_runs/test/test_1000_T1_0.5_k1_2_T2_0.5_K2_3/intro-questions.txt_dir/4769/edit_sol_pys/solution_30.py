

def is_anagram(s, t):
	if len(s) != len(t):
		return False
	return sorted(s) == sorted(t)

word = raw_input()

for i in range(len(word)):
	for j in range(i, len(word)):
		if is_anagram(word[:i], word[j+1:]):
			print word[:i]
			exit()

print -1
