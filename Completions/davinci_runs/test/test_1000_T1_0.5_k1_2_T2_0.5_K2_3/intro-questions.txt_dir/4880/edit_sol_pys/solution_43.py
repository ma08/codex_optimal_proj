

def decipher(n, m, last, cipher, plain):
	"""
	"""
	for i in range(m):
		if i < n:
			plain[i] = chr( ((ord(last[i]) - ord(cipher[i])) % 26) + 97 )
		else:
			plain[i] = chr( ((ord(plain[i-n]) - ord(cipher[i])) % 26) + 97 )

	return plain

def main():
	n, m = map(int, input().split())
	last = input()
	cipher = input()
	plain = [""] * m
	print(decipher(n, m, last, cipher, plain))

if __name__ == '__main__':
	main()
