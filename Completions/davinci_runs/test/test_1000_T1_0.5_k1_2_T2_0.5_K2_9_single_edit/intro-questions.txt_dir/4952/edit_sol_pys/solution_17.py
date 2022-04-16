

import sys

def main():
	votes = {}
	for line in sys.stdin:
		if line.strip() == "***": #break on ***
			break
		if line.strip() not in votes: #if key not in votes, add it
			votes[line.strip()] = 1
		else:
			votes[line.strip()] += 1 #if key in votes, increment
	max_votes = max(votes.values()) #find max votes
	if list(votes.values()).count(max_votes) == 1: #if max votes only occured once, print key with max votes
		print(list(votes.keys())[list(votes.values()).index(max_votes)]) 
	else:
		print("Runoff!") #if max votes occured more than once, print runoff

if __name__ == '__main__':
	main()
