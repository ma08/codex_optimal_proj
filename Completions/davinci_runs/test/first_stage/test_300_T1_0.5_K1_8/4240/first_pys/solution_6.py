

def is_rotated_string(s, t):
	for i in range(len(s)):
		if s[i:] + s[:i] == t:
			return True
	return False

def main():
	s = input()
	t = input()
	if is_rotated_string(s, t):
		print("Yes")
	else:
		print("No")

if __name__ == '__main__':
	main()