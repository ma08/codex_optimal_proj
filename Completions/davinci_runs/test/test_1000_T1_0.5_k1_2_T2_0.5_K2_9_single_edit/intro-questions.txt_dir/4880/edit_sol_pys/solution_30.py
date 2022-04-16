

#---------------------------------
# Code:

def decipher(n, m, last, cipher, plain):
	"""
	"""
	for i in range(m):
		if i < n:
			plain.append(chr( ((ord(last[i]) - ord(cipher[i])) % 26) + 97 ))
		else:
			plain.append(chr( ((ord(plain[i-n]) - ord(cipher[i])) % 26) + 97 ))


	return plain

def main():
	n, m = map(int, input().split())
	last = input()
	cipher = input()

	plain = []
	decipher(n, m, last, cipher, plain)
	print("".join(plain))

if __name__ == '__main__':
	main()
