

def main():
    # Get input
    player = int(input())  # pylint: disable=invalid-name
    num_questions = int(input())  # pylint: disable=invalid-name

    # Get the answers
    answers = [input().split() for _ in range(num_questions)]  # pylint: disable=invalid-name

    # Get the time limit
    time_limit = 3 * 60 + 30  # pylint: disable=invalid-name

    # Get the player who has the box initially.
    current_player = player  # pylint: disable=invalid-name

    # Iterate through the answers
    for time, answer in answers:  # pylint: disable=invalid-name
        # Check if the time limit is reached
        if int(time) > time_limit:
            break
        # Check if the answer is correct
        if answer == "T":
            # Pass the box to the next player
            current_player = (current_player + 1) % 8 or 8
        # Check if the answer is incorrect
        elif answer == "N":
            # Skip to the next question
            continue
        # Check if the answer is skipped
        elif answer == "P":
            # Pass the box to the next player
            current_player = (current_player + 1) % 8 or 8
            # Skip to the next question
            continue

    # Print the answer
    print(current_player)

if __name__ == "__main__":
    main()
