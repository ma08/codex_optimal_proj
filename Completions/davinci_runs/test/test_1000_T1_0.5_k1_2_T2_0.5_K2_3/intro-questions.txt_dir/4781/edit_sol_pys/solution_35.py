

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
        elif question[1] == "H":
            continue
        elif question[1] == "P":
            continue
        else:
            print("Error: invalid question response")
            exit()

    # Output
    print(player)

if __name__ == "__main__":
    main()
