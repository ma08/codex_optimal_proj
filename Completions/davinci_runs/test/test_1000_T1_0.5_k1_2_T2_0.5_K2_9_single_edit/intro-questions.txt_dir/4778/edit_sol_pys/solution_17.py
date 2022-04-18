
import sys

def efficiency_gap(votes):
    """
    votes: a list of tuples of the form (district, party_a_votes, party_b_votes)
    """
    # Get the total votes
    total_votes = sum([votes[i][1] + votes[i][2] for i in range(len(votes))])
    # Get the total votes for each party
    total_votes_a = sum([votes[i][1] for i in range(len(votes))])
    total_votes_b = sum([votes[i][2] for i in range(len(votes))])
    # Get the total votes for each district
    district_votes = {}
    for i in range(len(votes)):
        district = votes[i][0]
        if district not in district_votes:
            district_votes[district] = votes[i][1] + votes[i][2]
        else:
            district_votes[district] += votes[i][1] + votes[i][2]
    # Get the winner and wasted votes in each district
    district_results = {}
    for district in district_votes:
        votes_a = sum([votes[i][1] for i in range(len(votes)) if votes[i][0] == district])
        votes_b = sum([votes[i][2] for i in range(len(votes)) if votes[i][0] == district])
        if votes_a > votes_b:
            district_results[district] = ('A', votes_b, votes_a - (district_votes[district] // 2) - 1)
        else:
            district_results[district] = ('B', votes_a, votes_b - (district_votes[district] // 2) - 1)
    # Get the wasted votes for each party
    wasted_votes_a = sum([district_results[district][1] for district in district_results])
    wasted_votes_b = sum([district_results[district][2] for district in district_results])
    # Print the results
    for district in sorted(district_results):
        print(district_results[district][0], district_results[district][1], district_results[district][2])
    print(abs(wasted_votes_a - wasted_votes_b) / total_votes)

def main():
    # Read the input
    lines = sys.stdin.readlines()
    votes = []
    for i in range(1, len(lines)):
        votes.append(tuple(map(int, lines[i].split(' '))))
    # Get the efficiency gap
    efficiency_gap(votes)

if __name__ == '__main__':
    main()
