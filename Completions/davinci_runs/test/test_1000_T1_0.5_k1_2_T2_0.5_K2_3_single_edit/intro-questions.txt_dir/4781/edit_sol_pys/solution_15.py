

def main():
    # Read input
    player = int(input())
    num_questions = int(input())
    questions = []
    for i in range(num_questions):
        questions.append(input().split(" "))
    
    # Solve
    for question in questions:
        player = (player % 8) + 1
        if question[1] == "T" or question[1] == "t":
            player = (player % 8) + 1
        elif question[1] == "N" or question[1] == "n":
            pass
        elif question[1] == "P" or question[1] == "p":
            pass
        else:
            print("Error: invalid question response")
            exit()

    # Output
    print(player)

if __name__ == "__main__":
    main()
