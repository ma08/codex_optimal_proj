import sys

def rotate(string, rotationValue):
	newString = ""
	for c in string:
		newString += chr(((ord(c) - ord('A') + rotationValue) % 26) + ord('A'))
	return newString

def merge(string1, string2):
	newString = ""
	for i in range(len(string1)):
		newString += chr(((ord(string1[i]) - ord('A') + ord(string2[i]) - ord('A')) % 26) + ord('A'))
	return newString

def encrypt(string):
	if len(string) % 2 != 0:
		print("String length must be even.")
		return
	half1 = string[:len(string)//2]
	half2 = string[len(string)//2:]
	rotationValue1 = sum([ord(c) - ord('A') for c in half1])
	rotationValue2 = sum([ord(c) - ord('A') for c in half2])
	half1 = rotate(half1, rotationValue1)
	half2 = rotate(half2, rotationValue2)
	return merge(half1, half2)

def main():
	for line in sys.stdin:
		print(encrypt(line.strip()))

if __name__ == '__main__':
	main()
