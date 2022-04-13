

from collections import defaultdict

def efficiency_gap(districts):
    """
    The efficiency gap is a measure of how fair the districting is.
    It is the difference between the total number of wasted votes for
    the party that won the most seats and the party that won the fewest
    seats, divided by the total number of votes cast.
    """
    num_votes = sum(sum(p) for p in districts.values())
    wasted_votes = defaultdict(int)
    for district, district_votes in districts.items():
        if district_votes[0] > district_votes[1]:
            wasted_votes[district] = district_votes[0] - (sum(district_votes) / 2 + 1)
        else:
            wasted_votes[district] = district_votes[1] - (sum(district_votes) / 2 + 1)
    if sum(wasted_votes.values()) == 0:
        return 0
    return abs(sum(wasted_votes.values())) / num_votes


def main():
    P, D = [int(x) for x in input().strip().split()]
    districts = defaultdict(list)
    for i in range(P):
        d, a, b = [int(x) for x in input().strip().split()]
        districts[d].append((a, b))

    for district, district_votes in districts.items():
        votes_a = sum(p[0] for p in district_votes)
        votes_b = sum(p[1] for p in district_votes)
        if votes_a > votes_b:
            print('A', votes_a - (votes_a / 2 + 1), votes_b - (votes_b / 2 + 1))
        else:
            print('B', votes_a - (votes_a / 2 + 1), votes_b - (votes_b / 2 + 1))

    print(efficiency_gap(districts))


if __name__ == '__main__':
    main()
