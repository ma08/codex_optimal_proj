

def efficiencyGap(precincts, districts):
    # A is party A, B is party B
    A, B = 0, 0
    for d in range(1, districts+1):
        # Find the winning party
        votesA, votesB = 0, 0
        for p in precincts:
            if p[0] == d:
                votesA += p[1]
                votesB += p[2]
        if votesA > votesB:
            A += 1
        else:
            B += 1
        # Find the wasted votes
        print("A", votesB, votesA-votesB-1)
        print("B", votesA, votesB-votesA-1)
    V = sum([sum(p[1:3]) for p in precincts])
    wA = sum([p[2] for p in precincts if p[1] > p[2]])
    wB = sum([p[1] for p in precincts if p[1] < p[2]])
    print("{0:.10f}".format(abs(wA-wB)/V))

efficiencyGap([[1, 100, 200], [2, 100, 99], [3, 100, 50], [3, 100, 50], [2, 100, 98]], 3)
efficiencyGap([[3, 100, 99], [2, 100, 99], [1, 100, 99], [4, 100, 99]], 4)
