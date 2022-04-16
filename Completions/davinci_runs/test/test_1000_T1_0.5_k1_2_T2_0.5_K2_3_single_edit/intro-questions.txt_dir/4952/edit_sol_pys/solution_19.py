'''
Name: file.py
Author: Anila Hoxha
Created: 02/02/2020
Description: Write a program file.py that takes as input a sequence of names of candidates in a
presidential election, one per line, and prints out the name of the winner of the election. If no
candidate wins a majority of the votes, print the word Runoff!. A candidate wins a majority of
the votes if they receive strictly more than half of the votes. The end of the sequence of names
is marked by a line containing the word ***.
'''

import sys

def main():
    votes = []
    for line in sys.stdin:
        if line.strip() != '***':
            votes.append(line.strip())
        else:
    # Find the maximum number of votes
            break
    max_votes = 0
    for i in set(votes):
        if votes.count(i) > max_votes:
            max_votes = votes.count(i)
    # If the number of votes is greater than half of the total votes, print the winner
            winner = i
    if max_votes > len(votes)/2:
        print(winner)
    else:
        print('Runoff!')

if __name__ == '__main__':
    main()
