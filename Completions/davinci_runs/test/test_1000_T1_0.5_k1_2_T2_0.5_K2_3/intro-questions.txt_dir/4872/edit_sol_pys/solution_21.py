
import sys

def main():
	n = int(sys.stdin.readline())
	clean_pushes = [int(x) for x in sys.stdin.readline().split()]
	current_cleanness = 0
	cleanup_counter = 0
	for day in range(1, 366):
		if day in clean_pushes:
			current_cleanness += (day - clean_pushes.index(day))
		else:
			current_cleanness += 1
		if current_cleanness >= 20:
			cleanup_counter += 1
			current_cleanness = 0
	print(cleanup_counter)

if __name__ == '__main__':
	main()
