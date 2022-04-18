

def main():
    # Read input
    player = int(input()) # 1-8
    num_questions = int(input()) # 0-50
    questions = []
    for i in range(num_questions):
        questions.append(input().split()) # [question, answer]
    
    # Solve
    for question in questions:
        player = (player % 8) + 1
        if question[1] == "T": # True
            player = (player % 8) + 1
        elif question[1] == "N": # False
            pass
        elif question[1] == "P": # Neither
            pass
        else:
            print("Error: invalid question response")
            exit()

    # Output
    print(player)

if __name__ == "__main__":
    main()
