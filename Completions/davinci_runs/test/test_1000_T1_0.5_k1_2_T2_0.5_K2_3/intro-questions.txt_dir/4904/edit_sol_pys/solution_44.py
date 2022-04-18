

import sys

def main():
    # read input
    record = sys.stdin.readline().strip()

    # keep track of score for each player
    alice = 0
    barbara = 0

    # loop through the record in steps of 2
    for i in range(0, len(record), 2):
        # Alice scored
        if record[i] == 'A': alice += int(record[i+1])
        # Barbara scored
        else: barbara += int(record[i+1])
        # if alice's score is greater than 11
        if alice > 11:
            # if alice's score is greater than barbara's score by 2
            if alice - barbara >= 2:
                # print alice
                print('A')
                # end program
                return
            # if alice's score is not greater than barbara's score by 2
            else:
                # subtract from alice's score
                alice -= int(record[i+1])
        # if barbara's score is greater than 11
        if barbara > 11:
            # if barbara's score is greater than alice's score by 2
            if barbara - alice >= 2:
                # print barbara
                print('B')
                # end program
                return
            # if barbara's score is not greater than alice's score by 2
            else:
                # subtract from barbara's score
                barbara -= int(record[i+1])

    # print the winner
    if alice > barbara:
        print('A')
    else:
        print('B')

if __name__ == '__main__':
    main()
