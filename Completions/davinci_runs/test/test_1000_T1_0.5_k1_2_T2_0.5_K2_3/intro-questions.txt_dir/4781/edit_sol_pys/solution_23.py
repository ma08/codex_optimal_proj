

def main():
    # Read input
    player = int(input())  # 1-8
    num_questions = int(input())  # 1-50
    questions = []
    for i in range(num_questions):
        questions.append(input().split())
    
    # Solve the problem
    for question in questions:
        player = (player % 8) + 1
        if question[0] == "T":
            player = (player % 8) + int(question[1])
        elif question[0] == "N":
            player = (player % 8) + int(question[1])
        elif question[0] == "P":
            player = (player % 8) + int(question[1])
        else:
            print("Error: invalid question response")
            exit()

    # Output
    print(player)

if __name__ == "__main__":
    main()
