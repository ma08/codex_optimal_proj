

def main():
    # Read input
    player = int(input())
    num_questions = int(input())
    questions = []
    for i in range(num_questions):
        questions.append(list(input().split()))
    
    # Solve
    for question in questions:
        player = (player % 8) + 1
        if question[1] == 'T':  # Truth
            player = (player % 8) + 1
        elif question[1] == 'N':  # Dare
            pass
        elif question[1] == 'P':  # Pass
            pass
        else:
            print('Error: invalid question response')
            exit()

    # Output
    print(player)

if __name__ == '__main__':
    main()
