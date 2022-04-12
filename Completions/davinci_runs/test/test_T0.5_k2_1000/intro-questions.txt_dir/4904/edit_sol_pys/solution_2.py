

# ----- Imports -----

import sys

# ----- Functions -----

def calculate_winner(score):
	if score[0] >= score[1]:
		return 0
	else:
		return 1

def main(args):
	score = [0, 0]
	for i in range(0, len(args[1]), 2):
		score[int(args[1][i])] += int(args[1][i+1])
		if score[0] >= 11 or score[1] >= 11:
			if abs(score[0] - score[1]) >= 2:
				print("A" if calculate_winner(score) == 0 else "B", end="")
				break

# ----- Main -----

if __name__ == '__main__':
	main(sys.argv)
