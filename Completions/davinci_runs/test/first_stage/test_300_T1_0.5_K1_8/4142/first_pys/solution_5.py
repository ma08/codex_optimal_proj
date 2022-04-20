

#s = input()
s = "RUDLUDR"

def is_playable(s):
	odd = ["R", "U", "D"]
	even = ["L", "U", "D"]
	for i in range(len(s)):
		if i%2 == 0:
			if s[i] not in odd:
				return "No"
		else:
			if s[i] not in even:
				return "No"
	return "Yes"

print(is_playable(s))