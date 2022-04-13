

def main():
    # Read input
    player = int(input())
    num_questions = int(input())
    questions = []
    for i in range(num_questions):
        questions.append(input().split())
    
    # Solve
    for question in questions:
        player = (player % 8) + 1
        if question[1] == "T":  # Truth: next player
            player = (player % 8) + 1
        elif question[1] == "N":  # Dare: same player
            pass
        elif question[1] == "P":  # Pass: previous player
            pass
        else:
            print("Error: invalid question response")
            exit()

    # Output
    print(player)

if __name__ == "__main__":
    main()
