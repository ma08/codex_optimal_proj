

from sys import stdin

def main():
	board = []
	for line in stdin:
		board.append(line.rstrip())
	white = []
	black = []
	for i in range(8):
		for j in range(8):
			piece = board[i][j]
			if piece.isupper():
				white.append((piece, j+1, i+1))
			elif piece.islower():
				black.append((piece, j+1, i+1))
	white.sort(key=lambda x: (x[1], x[2]))
	black.sort(key=lambda x: (x[1], -x[2]))
	white = [x[0] + chr(x[1]+96) + str(x[2]) for x in white]
	black = [x[0] + chr(x[1]+96) + str(x[2]) for x in black]
	print('White: ' + ','.join(white))
	print('Black: ' + ','.join(black))

if __name__ == '__main__':
	main()
