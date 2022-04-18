

def efficiencyGap(p):
    # p is a list of lists, where p[i] is a list of the form [district, partyAvotes, partyBvotes]
    # For example, [[1, 100, 200], [2, 100, 99], [3, 100, 50], [3, 100, 50], [2, 100, 98]]
    # There are 3 districts, each with a different number of precincts
    # District 1 has 1 precinct, district 2 has 2 precincts, and district 3 has 2 precincts
    # District 1 has 100 votes for party A and 200 votes for party B
    # District 2 has 100 votes for party A and 99 votes for party B
    # District 2 has 100 votes for party A and 50 votes for party B
    # District 2 has 100 votes for party A and 50 votes for party B
    # District 2 has 100 votes for party A and 98 votes for party B
    # The total number of votes is 100+200+100+99+100+50+100+50+100+98=897
    # The number of wasted votes for party A is 200+99+50+50+98=497
    # The number of wasted votes for party B is 100+100+100=300
    # The efficiency gap is (497-300)/897=0.1665
    # The efficiency gap must be between -0.5 and 0.5
    # If the efficiency gap is negative, this means that party B is more efficient than party A
    # If the efficiency gap is positive, this means that party A is more efficient than party B
    # If the efficiency gap is 0, then both parties are equally efficient
    # Your function should return the efficiency gap, rounded to 10 decimal places

efficiencyGap([[1, 100, 200], [2, 100, 99], [3, 100, 50], [3, 100, 50], [2, 100, 98]], 3)
efficiencyGap([[3, 100, 99], [2, 100, 99], [1, 100, 99], [4, 100, 99]], 4)
