

from sys import stdin, stdout
from math import floor

def main():
    P, D = [int(i) for i in stdin.readline().split()]
    districts = [[] for i in range(0, D)]
    for i in range(0, P):
        district, A, B = [int(i) for i in stdin.readline().split()]
        districts[district-1].append([A, B])
    totalVotes = 0
    wA, wB = 0, 0
    for district in districts:
        totalVotes += sum([sum(precinct) for precinct in district])
        votesA, votesB = sum([precinct[0] for precinct in district]), sum([precinct[1] for precinct in district])
        if votesA > votesB:
            stdout.write("A\n")
            wA += votesB
            wB += votesA - floor((votesA+votesB)/2) - 1
        else:
            stdout.write("B\n")
            wA += votesA
            wB += votesB - floor((votesA+votesB)/2) - 1
    stdout.write("{0} {1}\n".format(wA, wB))
    stdout.write("{0}\n".format(abs(wA-wB)/totalVotes)) 

if __name__ == "__main__":
    main()
