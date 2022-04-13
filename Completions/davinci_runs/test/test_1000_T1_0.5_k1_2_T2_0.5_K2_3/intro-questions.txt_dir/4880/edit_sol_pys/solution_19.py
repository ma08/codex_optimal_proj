
import sys
def decipher(n, m, last, cipher):
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
	n, m = map(int, sys.stdin.readline().split())
	last = sys.stdin.readline()
	cipher = sys.stdin.readline()
	print(decipher(n, m, last, cipher))

if __name__ == '__main__':
	main()
