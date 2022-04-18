

def main():
    # parse input
    game = input()
    alice = 0  # alice's score
    barbara = 0  # barbara's score

    for i in range(len(game)):
        if game[i] == 'A':  # when alice scores
            if game[i + 1] == '1':  # when alice scores 1 point
                alice += 1
            else:  # when alice scores 2 points
                alice += 2
        else:  # when barbara scores
            if game[i + 1] == '1':  # when barbara scores 1 point
                barbara += 1
            else:  # when barbara scores 2 points
                barbara += 2

    # determine the winner
    if alice == 11 and barbara == 10:  # alice wins by 2
        print('A')
    elif barbara == 11 and alice == 10:  # barbara wins by 2
        print('B')
    elif alice > barbara:  # alice wins
        print('A')
    elif barbara > alice:  # barbara wins
        print('B')
    else:  # error
        print('error')

if __name__ == '__main__':
    main()
