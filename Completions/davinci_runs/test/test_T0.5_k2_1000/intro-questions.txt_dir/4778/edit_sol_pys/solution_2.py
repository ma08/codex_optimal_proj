

def solve(input):
    """
    >>> solve('5 3\\n1 100 200\\n2 100 99\\n3 100 50\\n4 100 50\\n5 100 98')\\n'
    'B 100 49\\nA 1 197\\nA 49 100\\n0.1965897693\\n'
    >>> solve('4 4\\n3 100 99\\n2 100 99\\n1 100 99\\n4 100 99\\n5 100 99')\\n'
    'A 0 99\\nA 0 99\\nA 0 99\\nA 0 99\\n0.4974874372\\n'
    """
    P, D = [int(x) for x in input.split()[0:2]]  # P - number of precincts, D - number of districts
    precincts = []
    for i in range(P):
        precincts.append([int(x) for x in input.split()[2:5]])  # list of precincts
    districts = {}
    for precinct in precincts:
        if precinct[0] not in districts:  # precinct[0] - number of district
            districts[precinct[0]] = [[precinct[1], precinct[2]]]
        else:
            districts[precinct[0]].append([precinct[1], precinct[2]])
    districts_results = []  # list of districts results
    for district in districts:
        votes = districts[district]  # list of votes in district
        votes_a = sum([v[0] for v in votes])
        votes_b = sum([v[1] for v in votes])
        if votes_a > votes_b:
            districts_results.append(['A', votes_a - (votes_a + votes_b) / 2 - 1, votes_b])
        else:
            districts_results.append(['B', votes_a, votes_b - (votes_a + votes_b) / 2 - 1])
    total_votes = sum([districts_results[i][1] + districts_results[i][2] for i in range(len(districts_results))])  # total votes
    total_wasted_a = sum([districts_results[i][1] for i in range(len(districts_results))])  # total wasted votes for A
    total_wasted_b = sum([districts_results[i][2] for i in range(len(districts_results))])  # total wasted votes for B
    output = ''
    for district in districts_results:
        output = output + district[0] + ' ' + str(district[1]) + ' ' + str(district[2]) + '\\n'
    output = output + str(abs(total_wasted_a - total_wasted_b) / float(total_votes))
    return output


if __name__ == '__main__':
    import doctest
    doctest.testmod()
