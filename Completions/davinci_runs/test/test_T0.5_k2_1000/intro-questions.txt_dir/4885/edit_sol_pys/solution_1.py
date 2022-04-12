

from sys import stdin

def main():
	board = []
	for line in stdin:
		board.append(line.rstrip())
	white = []
	black = []
	for i in range(1,9):
		for j in range(1,9):
			piece = board[i-1][j-1]
			if piece.isupper():
				white.append((piece, j, i))
			elif piece.islower():
				black.append((piece, j, i))
	white.sort(key=lambda x: (x[1], x[2]))
	black.sort(key=lambda x: (x[1], -x[2]))
	white = [x[0] + chr(x[1]+96) + str(x[2]) for x in white] # chr(x[1]+96) is the same as chr(x[1]+ord('a')-1)
	black = [x[0] + chr(x[1]+96) + str(x[2]) for x in black] # chr(x[1]+96) is the same as chr(x[1]+ord('a')-1)
	print('White: ' + ','.join(white))
	print('Black: ' + ','.join(black))

if __name__ == '__main__':
	main()
