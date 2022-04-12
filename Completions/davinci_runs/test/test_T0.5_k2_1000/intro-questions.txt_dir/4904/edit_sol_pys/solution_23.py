

def main():
    # parse the input
    game = input("Enter the game: ")
    alice = 0
    barbara = 0

    for i in range(0, len(game), 2):
        if game[i] == 'A':
            if game[i + 1] == '1' or game[i + 1] == '2':
                alice += 1
            else:
                alice += 2
        else:
            if game[i + 1] == '1' or game[i + 1] == '2':
                barbara += 1
            else:
                barbara += 2

    # determine the winner
    if alice == 11 and barbara == 10:
        print('Alice')
    elif barbara == 11 and alice == 10:
        print('Barbara')
    elif alice > barbara:
        print('Alice')
    elif barbara > alice:
        print('Barbara')
    else:
        print('error')

if __name__ == '__main__':
    main()
