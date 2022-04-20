

import sys

def main():
	for line in sys.stdin:
		line = line.strip()
		if line == '':
			continue
		
		numbers = line.split('+')
		for i in range(len(numbers)):
			if '-' in numbers[i]:
				numbers[i] = numbers[i].split('-')
				for j in range(len(numbers[i])):
					numbers[i][j] = int(numbers[i][j])
		
		result = numbers[0][0]
		for i in range(1, len(numbers)):
			if isinstance(numbers[i], list):
				result -= numbers[i][0]
				for j in range(1, len(numbers[i])):
					result += numbers[i][j]
			else:
				result -= numbers[i]
		
		print(result)
		
if __name__ == '__main__':
	main()