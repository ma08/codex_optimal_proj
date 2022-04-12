

def efficiency_gap(precincts, districts, partyA, partyB):
    # A is party A, B is party B
    A = 0
    B = 0
    for d in range(1, districts+1):
        # Find the winning party
        votesA = 0
        votesB = 0
        for p in precincts:
            if p[0] == d:
                votesA += p[partyA]
                votesB += p[partyB]
        if votesA > votesB:
            A += 1
        else:
            B += 1
        # Find the wasted votes
            print("A", votesB, votesA - votesB - 1)
        else: 
            print("B", votesA, votesB - votesA - 1)
    V = sum([sum(p[partyA:partyB+1]) for p in precincts])
    wA = sum([p[partyB] for p in precincts if p[partyA] > p[partyB]])
    wB = sum([p[partyA] for p in precincts if p[partyA] < p[partyB]])
    print("{0:.10f}".format(abs(wA - wB) / V))

efficiency_gap([[1, 100, 200], [2, 100, 99], [3, 100, 50], [3, 100, 50], [2, 100, 98]], 3, 1, 2)
efficiency_gap([[3, 100, 99], [2, 100, 99], [1, 100, 99], [4, 100, 99]], 4, 1, 2)
