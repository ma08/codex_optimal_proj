

import sys

def rotate(string, rotationValue):
	newString = ""
	for c in string:
		newString += chr(((ord(c) - ord('A') + rotationValue) % 26) + ord('A')) # rotates each character
	return newString

def merge(string1, string2):
	newString = ""
	for i in range(len(string1)):
		newString += chr(((ord(string1[i]) - ord('A') + ord(string2[i]) - ord('A')) % 26) + ord('A')) # merges the two strings
	return newString

def decrypt(string):
	if len(string) % 2 != 0: # if the length of the string is odd
		print("String length must be even.")
		return
	half1 = string[:len(string)//2] # first half of the string
	half2 = string[len(string)//2:] # second half of the string
	rotationValue1 = sum([ord(c) - ord('A') for c in half1]) # finds the rotation value of the first half
	rotationValue2 = sum([ord(c) - ord('A') for c in half2]) # finds the rotation value of the second half
	half1 = rotate(half1, rotationValue1) # rotates the first half
	half2 = rotate(half2, rotationValue2) # rotates the second half
	return merge(half1, half2) # merges the two halves

def main():
	for line in sys.stdin:
		print(decrypt(line.strip()))

if __name__ == '__main__':
	main()
