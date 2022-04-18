

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
        if question[1] == "T":
            player = (player % 8) + 1
        elif question[1] == "N" and player == 1:
            player = 2
        elif question[1] == "N" and player == 2:
            player = 1
        elif question[1] == "N" and player == 3:
            player = 4
        elif question[1] == "N" and player == 4:
            player = 3
        elif question[1] == "N" and player == 5:
            player = 6
        elif question[1] == "N" and player == 6:
            player = 5
        elif question[1] == "N" and player == 7:
            player = 8
        elif question[1] == "N" and player == 8:
            player = 7
        elif question[1] == "N" and player == 9:
            pass
        elif question[1] == "P" and player == 1:
            player = 2
        elif question[1] == "P" and player == 2:
            player = 1
        elif question[1] == "P" and player == 3:
            player = 4
        elif question[1] == "P" and player == 4:
            player = 3
        elif question[1] == "P" and player == 5:
            player = 6
        elif question[1] == "P" and player == 6:
            player = 5
        elif question[1] == "P" and player == 7:
            player = 8
        elif question[1] == "P" and player == 8:
            player = 7
        elif question[1] == "P" and player == 9:
            pass
        else:
            print("Error: invalid question response")
            exit()

    # Output
    print(player)

if __name__ == "__main__":
    main()
