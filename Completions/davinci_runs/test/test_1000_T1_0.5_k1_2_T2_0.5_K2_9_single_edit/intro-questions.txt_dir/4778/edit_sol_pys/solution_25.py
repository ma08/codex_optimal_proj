

def efficiencyGap(precincts, districts):
    # A is party A, B is party B
    A, B = 0, 0
    V = sum([sum(p[1:3]) for p in precincts])
    wA = sum([p[2] for p in precincts if p[1] > p[2]])
    wB = sum([p[1] for p in precincts if p[1] < p[2]])
    return "{0:.10f}".format(abs(wA-wB)/V)

print(efficiencyGap([[1, 100, 200], [2, 100, 99], [3, 100, 50], [3, 100, 50], [2, 100, 98]], 3))
print(efficiencyGap([[3, 100, 99], [2, 100, 99], [1, 100, 99], [4, 100, 99]], 4))
