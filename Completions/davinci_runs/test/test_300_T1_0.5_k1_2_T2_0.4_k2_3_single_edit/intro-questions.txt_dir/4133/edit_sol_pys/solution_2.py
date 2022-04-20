
import sys

def get_word_count(filename):
	word_count = 0
	
	with open(filename) as f:
		for line in f:
			words = line.split()
			word_count += len(words)
			
	return word_count
	
def get_char_count(filename):
	char_count = 0
	
	with open(filename) as f:
		for line in f:
			char_count += len(line)
			
	return char_count
	
def get_line_count(filename):
	line_count = 0
	
	with open(filename) as f:
		for line in f:
			line_count += 1
			
	return line_count


def main():
	filename = sys.argv[1]
	print(get_word_count(filename))
	print(get_char_count(filename))
	print(get_line_count(filename))

if __name__ == '__main__':
	main()
