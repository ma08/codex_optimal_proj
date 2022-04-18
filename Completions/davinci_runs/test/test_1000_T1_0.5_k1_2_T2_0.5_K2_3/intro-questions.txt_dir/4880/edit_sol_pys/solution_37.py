

#-----------------------------------
# Code:

def decipher(n, m, last, cipher):
	"""
	"""
	plain = ""
	for i in range(m):
		if i < n:
			plain += chr( ((ord(cipher[i]) - ord(last[i])) % 26) + 97 )
		else:
			plain += chr( ((ord(cipher[i]) - ord(plain[i-n])) % 26) + 97 )

	return plain

def main():
	n, m = map(int, input().split())
	last = input()
	cipher = input()
	print(decipher(n, m, last, cipher))

if __name__ == '__main__':
	main()
