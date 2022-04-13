

from sys import stdin

def main():
	board = []
	for line in stdin:
		board.append(line.rstrip())
	white = []
	black = []
	for i in range(1,9):
		for j in range(1,9):
			piece = board[i][j]
			if piece.isupper():
				white.append((piece, i, j))
			elif piece.islower():
				black.append((piece, i, j))
	white.sort(key=lambda x: (x[2], x[1]))
	black.sort(key=lambda x: (x[2], -x[1]))
	white = [x[0] + chr(x[2]+96) + str(x[1]) for x in white if x[0] != 'K']
	black = [x[0] + chr(x[2]+96) + str(x[1]) for x in black if x[0] != 'k']
	print('White: ' + ','.join(white))
	print('Black: ' + ','.join(black))

if __name__ == '__main__':
	main()
