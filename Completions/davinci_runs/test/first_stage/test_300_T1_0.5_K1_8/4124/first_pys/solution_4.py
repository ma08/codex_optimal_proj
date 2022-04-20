

def solve(s, t):
	# If s == t, then return 0.
	if s == t:
		return 0

	# If s != t and len(s) == len(t), then return len(s).
	if len(s) == len(t):
		return len(s)

	# Otherwise, we can't make them equal.
	return -1


def main():
	s = input()
	t = input()
	print(solve(s, t))


if __name__ == '__main__':
	main()