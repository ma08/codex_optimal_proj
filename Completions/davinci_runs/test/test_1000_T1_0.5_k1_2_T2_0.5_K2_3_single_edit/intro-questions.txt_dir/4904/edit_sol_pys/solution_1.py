

def main():
    # parse input
    game = input("")
    alice = 0
    barbara = 0

    for i in range(len(game)):
        if game[i] == 'A':
            if game[i + 1] == '1':
                alice += 1
            else:
                alice += 2
        else:
            if game[i + 1] == '1':
                barbara += 1
            else:
                barbara += 2

    # determine the winner
    if alice == 11 and barbara == 10:
        print('A', end='')
    elif barbara == 11 and alice == 10:
        print('B', end='')
    elif alice > barbara:
        print('A', end='')
    elif barbara > alice:
        print('B', end='')
    else:
        print('error', end='')

if __name__ == '__main__':
    main()
