

def main():
    # Read input
    player = int(raw_input())
    num_questions = int(raw_input())
    questions = []
    for i in range(num_questions):
        questions.append(raw_input().split())
    
    # Solve
    for question in questions:
        player = (player % 8) + 1 # player is 1-indexed
        if question[1] == "T": # Truth
            player = (player % 8) + 1 # player is 1-indexed
        elif question[1] == "N": # Dare
            pass
        elif question[1] == "P":
            pass
        else:
            print("Error: invalid question response")
            exit()

    # Output
    print(player)

if __name__ == "__main__":
    main()
