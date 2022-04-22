

import sys
import re

def get_file_line(file_name):
	with open(file_name, "r") as f:
		return re.split("\n", f.read())

def main(file_name):
	lines = get_file_line(file_name)
	for line in lines:
		print(line)

if __name__ == "__main__":
	main(sys.argv[1])
