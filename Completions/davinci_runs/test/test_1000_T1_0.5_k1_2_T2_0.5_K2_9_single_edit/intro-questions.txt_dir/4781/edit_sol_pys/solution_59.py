

def main():
    # Read input
    player = int(input())
    num_questions = int(input())
    questions = []
    for i in range(num_questions):
        questions.append(input().split())
    
    # Solve
    for question in questions:        
        if question[1] == "T":            
            player = (player + 2) % 8
        elif question[1] == "N":            
            player = (player + 1) % 8
        elif question[1] == "P":            
            pass
            player = (player + 1) % 8
        else:
            print("Error: invalid question response")
            exit()

    # Output
    print(player)

if __name__ == "__main__":
    main()
