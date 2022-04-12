

import sys

def main():
	num_players = sys.stdin.readline()
	players = []
	for i in range(int(num_players)):
		players.append(sys.stdin.readline().rstrip())
	if sorted(players) == players and len(set(players)) == len(players):
		print('INCREASING')
	elif sorted(players, reverse=True) == players and len(set(players)) == len(players):
		print('DECREASING')
	else:
		print('NEITHER')

if __name__ == '__main__':
	main()
