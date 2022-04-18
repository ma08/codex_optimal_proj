

def main():
    # Read input
    player = int(raw_input())
    num_questions = int(raw_input())
    questions = []
    for i in range(num_questions):
        questions.append(raw_input().split())
    
    # Solve
    for question in questions:
        player = (player % 8) + 1
        if question[1] == "T":
            player = (player % 8) + 1
            pass
        elif question[1] == "H":
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
