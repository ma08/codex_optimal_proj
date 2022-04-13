

def main():
    """
    The main entry point for the script.
    """
    # Read the input data.
    precincts, districts = [int(x) for x in input().split()]
    data = [[int(x) for x in input().split()] for _ in range(precincts)]

    # Get the total votes per district.
    total_votes = [[0, 0] for _ in range(districts)]
    for precinct in data:
        total_votes[precinct[0] - 1][0] += precinct[1]
        total_votes[precinct[0] - 1][1] += precinct[2]

    # Get the winners and wasted votes per district.
    winners = []
    wasted_votes = [[0, 0] for _ in range(districts)]
    for district in range(districts):
        if total_votes[district][0] > total_votes[district][1]:
            winners.append('A')
            wasted_votes[district][0] = total_votes[district][0] - (total_votes[district][0] // 2 + 1)
            wasted_votes[district][1] = total_votes[district][1]
        else:
            winners.append('B')
            wasted_votes[district][0] = total_votes[district][0]
            wasted_votes[district][1] = total_votes[district][1] - (total_votes[district][1] // 2 + 1)

    # Print the output.
    for district in range(districts):
        print(winners[district], wasted_votes[district][0], wasted_votes[district][1])

    # Calculate and print the efficiency gap.
    efficiency_gap = sum([wasted_votes[district][0] for district in range(districts)]) - sum([wasted_votes[district][1] for district in range(districts)])
    efficiency_gap /= sum([total_votes[district][0] + total_votes[district][1] for district in range(districts)])
    print(abs(efficiency_gap))

# Execute the main function.
if __name__ == '__main__':
    main()
