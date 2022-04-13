"""
Author: Eric J. Ma

Date: 2016-07-01

This is a solution to the efficiency gap problem.
"""


def main():
    """
    Main function
    """
    # Get input
    p, d = [int(x) for x in input().split()]
    precincts = []
    for i in range(p):
        precincts.append([int(x) for x in input().split()])
    # Get the districts, and populate them with precincts
    districts = []
    for i in range(d):
        districts.append([])
    for precinct in precincts:
        districts[precinct[0]-1].append(precinct)
    # Get the results and the efficiency gap
    results = []  # [winner, lost_votes, excess_votes]
    total_votes = 0
    total_lost_votes = 0
    total_excess_votes = 0
    for district in districts:
        a_votes = sum([precinct[1] for precinct in district])
        b_votes = sum([precinct[2] for precinct in district])
        if a_votes > b_votes:
            winner = 'A'
            lost_votes = b_votes
            excess_votes = a_votes - ((len(district) // 2) + 1)
        else:
            winner = 'B'
            lost_votes = a_votes
            excess_votes = b_votes - ((len(district) // 2) + 1)
        results.append([winner, lost_votes, excess_votes])
        total_votes += a_votes + b_votes
        total_lost_votes += lost_votes
        total_excess_votes += excess_votes
    # Print the results
    for result in results:
        print(result[0], result[1], result[2])
    # Print the efficiency gap
    print(abs(total_lost_votes - total_excess_votes) / total_votes)


if __name__ == "__main__":
    main()
