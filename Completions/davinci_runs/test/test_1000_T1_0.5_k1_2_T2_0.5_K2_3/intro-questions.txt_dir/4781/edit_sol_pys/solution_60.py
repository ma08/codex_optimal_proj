

def main():
    # Get input
    player = int(input())
    num_answers = int(input())

    # Get the answers
    answers = [input().split() for _ in range(num_answers)]

    # Get the time limit
    time_limit = 3 * 60 + 30

    # Get the ID of the player who has the box initially
    current_player_id = player

    # Iterate through the answers
    for time, answer in answers[:time_limit]:
        # Check if the time limit is reached
        if int(time) > time_limit:
            break
        # Check if the answer is correct
        if answer == "T":
            # Pass the box to the next player
            current_player_id = (current_player_id + 1) % 8 or 8
        # Check if the answer is incorrect
        elif answer == "N":
            # Skip to the next question
            continue
        # Check if the answer is skipped
        elif answer == "P":
            # Pass the box to the next player
            current_player_id = (current_player_id + 1) % 8 or 8
            # Skip to the next question
            continue

    # Print the answer
    print(current_player_id)

if __name__ == "__main__":
    main()
