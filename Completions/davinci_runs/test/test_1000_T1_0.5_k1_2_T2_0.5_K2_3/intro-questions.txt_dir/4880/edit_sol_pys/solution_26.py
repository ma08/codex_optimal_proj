#-----------------------------------
# File:
# Author:
# Date:
#-----------------------------------

#-----------------------------------
# Code:

def decipher(n, m, last, cipher):
	deciphers a ciphertext

	Parameters:
		n (int): the number of characters in the last word
		m (int): the number of characters in the ciphertext
		last (str): the last word in the plaintext
		cipher (str): the ciphertext

	Returns:
		plain (str): the plaintext
	"""
	"""
	plain = ""
	for i in range(m):
		if i < n:
			plain += chr( ((ord(last[i]) - ord(cipher[i])) % 26) + 97 )
		else:
			plain += chr( ((ord(plain[i-n]) - ord(cipher[i])) % 26) + 97 )

	return plain

def main():
	n, m = map(int, input().split())
	last = input()
	cipher = input()
	print(decipher(n, m, last, cipher))

if __name__ == '__main__':
	main()
