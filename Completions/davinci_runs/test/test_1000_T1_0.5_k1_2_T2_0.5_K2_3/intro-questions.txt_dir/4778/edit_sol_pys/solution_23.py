

from collections import defaultdict

def efficiency_gap(precincts):
    """
    The efficiency gap is a measure of how fair the redistricting is.
    It is the difference between the total number of wasted votes for
    the party that won the most seats and the party that won the fewest
    seats, divided by the total number of votes cast.
    """
    num_votes = sum(sum(p) for p in precincts.values())
    wasted_votes = defaultdict(int)
    for district, precinct_votes in precincts.items():
        if precinct_votes[0] > precinct_votes[1]:
            wasted_votes[district] = precinct_votes[0] - (sum(precinct_votes) / 2 + 1)
        else:
            wasted_votes[district] = precinct_votes[1] - (sum(precinct_votes) / 2 + 1)
    if sum(wasted_votes.values()) == 0:
        return 0
    return abs(sum(wasted_votes.values())) / num_votes


def main():
    P, D = [int(x) for x in input().strip().split()]
    precincts = defaultdict(list)
    for i in range(P):
        d, a, b = [int(x) for x in input().strip().split()]
        precincts[d].append((a, b))

    for district, precinct_votes in precincts.items():
        votes_a = sum(p[0] for p in precinct_votes)
        votes_b = sum(p[1] for p in precinct_votes)
        if votes_a > votes_b:
            print('A', votes_a - (votes_a / 2 + 1), votes_b - (votes_b / 2 + 1))
        else:
            print('B', votes_a - (votes_a / 2 + 1), votes_b - (votes_b / 2 + 1))

    print(efficiency_gap(precincts))


if __name__ == '__main__':
    main()
