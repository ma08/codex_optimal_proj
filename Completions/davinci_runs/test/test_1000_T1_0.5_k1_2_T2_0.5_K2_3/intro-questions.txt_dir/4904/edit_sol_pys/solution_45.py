

import sys

def main():
    # read input
    record = sys.stdin.readline().strip()

    # keep track of score for each player
    alice = 0
    barbara = 0

    # loop through the records
    for i in range(0, len(record), 2):
        # if Alice scored
        if record[i] == 'A':
            # add to Alice's score
            alice += int(record[i+1])
            # if Alice's score is greater than 11
            if alice > 11:
                # if Alice's score is greater than Barbara's score by 2
                if alice - barbara >= 2:
                    # print Alice
                    print('A')
                    # end program
                    return
                # if Alice's score is not greater than Barbara's score by 2 or more
                else:
                    # subtract from Alice's score
                    alice -= int(record[i+1])
        # if Barbara scored
        else:
            # add to Barbara's score
            barbara += int(record[i+1])
            # if Barbara's score is greater than 11
            if barbara > 11:
                # if Barbara's score is greater than Alice's score by 2
                if barbara - alice >= 2:
                    # print Barbara
                    print('B')
                    # end program
                    return
                # if Barbara's score is not greater than Alice's score by 2
                else:
                    # subtract from Barbara's score
                    barbara -= int(record[i+1])

    # print the winner
    if alice > barbara:
        print('A')
    else:
        print('B')

if __name__ == '__main__':
    main()
