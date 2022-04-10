

def main():
	n = int(raw_input())
	prefixes = [raw_input() for _ in range(n-1)]
	suffixes = [raw_input() for _ in range(n-1)]
	print ''.join(['P' if prefixes[i] in suffixes else 'S' for i in range(n-1)])

if __name__ == '__main__':
	main()