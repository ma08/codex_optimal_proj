

def main():
    """
    The main entry point for the script.
    """
    # Read the input data.
    precincts, districts = [int(x) for x in input().split()] #creates a list of the number of precincts and districts
    data = [[int(x) for x in input().split()] for _ in range(precincts)] #creates a 2d list of the precincts and the number of votes for each candidate

    # Get the total votes per district.
    total_votes = [[0, 0] for _ in range(districts)] #creates a list of lists of the total number of votes for each district
    for precinct in data:
        total_votes[precinct[0] - 1][0] += precinct[1] #adds the number of votes for candidate A to the list
        total_votes[precinct[0] - 1][1] += precinct[2] #adds the number of votes for candidate B to the list

    # Get the winners and wasted votes per district.
    winners = [] #creates an empty list of winners
    wasted_votes = [[0, 0] for _ in range(districts)] #creates a list of lists of wasted votes
    for district in range(districts):
        if total_votes[district][0] > total_votes[district][1]: #if candidate A has more votes than candidate B
            winners.append('A') #adds A to the list of winners
            wasted_votes[district][0] = total_votes[district][0] - (total_votes[district][0] // 2 + 1) #calculates the number of wasted votes for candidate A
            wasted_votes[district][1] = total_votes[district][1] #calculates the number of wasted votes for candidate B
        else:
            winners.append('B') #adds B to the list of winners
            wasted_votes[district][0] = total_votes[district][0] #calculates the number of wasted votes for candidate A
            wasted_votes[district][1] = total_votes[district][1] - (total_votes[district][1] // 2 + 1) #calculates the number of wasted votes for candidate B

    # Print the output.
    for district in range(districts):
        print(winners[district], wasted_votes[district][0], wasted_votes[district][1])

    # Calculate and print the efficiency gap.
    efficiency_gap = sum([wasted_votes[district][0] for district in range(districts)]) - sum([wasted_votes[district][1] for district in range(districts)])
    efficiency_gap /= sum([total_votes[district][0] + total_votes[district][1] for district in range(districts)])
    print(abs(efficiency_gap)) #prints the absolute value of the efficiency gap

# Execute the main function.
if __name__ == '__main__':
    main()
