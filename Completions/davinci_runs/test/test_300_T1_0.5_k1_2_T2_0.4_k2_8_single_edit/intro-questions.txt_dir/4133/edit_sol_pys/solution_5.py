import os
import sys


def main():
	if len(sys.argv) < 2:
		print("Usage: python file.py <filename>")
		sys.exit(1)
	filename = sys.argv[1]
	if not os.path.exists(filename):
		print("Error: File '%s' not found" % filename)
		sys.exit(2)
	f = open(filename, "r")
	for line in f:
		print(line)
	f.close()

if __name__ == '__main__':
	main()
