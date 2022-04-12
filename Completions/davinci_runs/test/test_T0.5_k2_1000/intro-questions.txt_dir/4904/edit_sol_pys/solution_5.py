

def main():
    # parse input
    game = input()
    alice = 0
    barbara = 0

    for i in range(len(game) - 1):
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

    # determine the winner, if there is a tie, print 'error'
    if alice == 11 and barbara == 10:
        print('A')
    elif barbara == 11 and alice == 10:
        print('B')
    elif alice > barbara:
        print('A')
    elif barbara > alice:
        print('B')
    else:
        print('error')

if __name__ == '__main__':
    main()
