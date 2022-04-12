

def main():
    # parse input, and determine the winner, if there is a tie, print 'error'
    game = input()  # 'A1B2'
    alice = 0  # Alice's score
    barbara = 0  # Barbara's score

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
