

import sys

def main():
	votes = {}
	for line in sys.stdin:
		if line.strip() == "***":
			break
		if line.strip() not in votes:
			votes[line.strip()] = 1
		else:
			votes[line.strip()] += 1
	max_votes = max(votes.values())
	if list(votes.values()).count(max_votes) == 1:
		print(list(votes.keys())[list(votes.values()).index(max_votes)])
	else:
		print("Runoff!")
if __name__ == '__main__':
	main()
