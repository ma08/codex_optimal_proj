

from sys import stdin, stdout
from math import floor

def main():
    P, D = [int(i) for i in stdin.readline().split()]
    precincts = [[] for i in range(0, D)]
    for i in range(0, P):
        precinct, A, B = [int(i) for i in stdin.readline().split()]
        precincts[precinct-1].append([A, B])
    totalVotes = 0
    wA, wB = 0, 0
    for precinct in precincts:
        totalVotes += sum([sum(vote) for vote in precinct])*2
        votesA, votesB = sum([vote[0] for vote in precinct]), sum([vote[1] for vote in precinct])
        if votesA > votesB:
            stdout.write("A\n")
            wA += votesB
            wB += votesA - floor((votesA+votesB)/2) + 1
        else:
            stdout.write("B\n")
            wA += votesA
            wB += votesB - floor((votesA+votesB)/2) + 1
    stdout.write("{0} {1}\n".format(wA, wB))
    stdout.write("{0}\n".format(abs(wA-wB)/totalVotes))

if __name__ == "__main__":
    main()
