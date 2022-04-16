

from collections import defaultdict

def efficiency_gap(precincts):
    """
    The efficiency gap is a measure of how fair the districting is.
    It is the difference between the total number of wasted votes for
    the party that won the most seats and the party that won the fewest
    seats, divided by the total number of votes cast.
    """
    num_votes = sum(sum(p) for district, precinct_votes in precincts.items() for p in precinct_votes)
    wasted_votes = defaultdict(int)
    for district, precinct_votes in precincts.items():
        if precinct_votes[0] > precinct_votes[1]:
            wasted_votes[district] = precinct_votes[0] - (sum(precinct_votes) // 2 + 1)
        else:
            wasted_votes[district] = precinct_votes[1] - (sum(precinct_votes) // 2 + 1)
    if sum(wasted_votes.values()) == 0:
        return 0
    return abs(sum(wasted_votes.values())) / num_votes


def main():
    P, D = [int(x) for x in input().strip().split()]
    precincts = defaultdict(list)
    for i in range(P):
        d, a, b = [int(x) for x in input().strip().split()]
        precincts[d].append((a, b))

    for district, precinct_votes in precincts.items(): # for each district
        votes_a = sum(p[0] for p in precinct_votes) # sum of party a votes
        votes_b = sum(p[1] for p in precinct_votes) # sum of party b votes
        # print wasted votes for each party in each district
        if votes_a > votes_b:
            print('A', votes_a - (votes_a // 2 + 1), votes_b - (votes_b // 2 + 1)) # wasted votes for party a, wasted votes for party b
        else:
            print('B', votes_a - (votes_a // 2 + 1), votes_b - (votes_b // 2 + 1)) # wasted votes for party b, wasted votes for party a

    print(efficiency_gap(precincts))


if __name__ == '__main__':
    main()
