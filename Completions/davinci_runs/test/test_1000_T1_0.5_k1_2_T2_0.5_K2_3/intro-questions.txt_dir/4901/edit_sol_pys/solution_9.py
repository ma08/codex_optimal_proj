
import sys

def rotate(string, rotationValue):
	new_string = ""
	for c in string:
		new_string += chr(((ord(c) - ord('A') + rotationValue) % 26) + ord('A'))
	return new_string

def merge(string1, string2):
	new_string = ""
	for i in range(len(string1)):
		new_string += chr(((ord(string1[i]) - ord('A') + ord(string2[i]) - ord('A')) % 26) + ord('A'))
	return new_string

def decrypt(string):
	if len(string) % 2 != 0:
		print("String length must be even.")
		return
	half_1 = string[:len(string)//2]
	half_2 = string[len(string)//2:]
	rotation_value_1 = sum([ord(c) - ord('A') for c in half_1])
	rotation_value_2 = sum([ord(c) - ord('A') for c in half_2])
	half_1 = rotate(half_1, rotation_value_1)
	half_2 = rotate(half_2, rotation_value_2)
	return merge(half_1, half_2)

def main():
	for line in sys.stdin:
		print(decrypt(line.strip()))

if __name__ == '__main__':
	main()
