

import sys

def main():
    # read input
    record = sys.stdin.readline().strip()

    # keep track of score for each player
    Alice = 0
    Barbara = 0

    # loop through the record
    for i in range(0, len(record), 2):
        # if Alice scored
        if record[i] == 'A':
            # add to Alice's score
            Alice += int(record[i+1])
            # if Alice's score is greater than 11
            if Alice > 11:
                # if Alice's score is greater than Barbara's score by 2
                if Alice - Barbara >= 2:
                    # print Alice
                    print('A')
                    # end program
                    return
                # if Alice's score is not greater than Barbara's score by 2
                else:
                    # subtract from Alice's score
                    Alice -= int(record[i+1])
        # if Barbara scored
        else:
            # add to Barbara's score
            Barbara += int(record[i+1])
            # if Barbara's score is greater than 11
            if Barbara > 11:
                # if Barbara's score is greater than Alice's score by 2
                if Barbara - Alice >= 2:
                    # print Barbara
                    print('B')
                    # end program
                    return
                # if Barbara's score is not greater than Alice's score by 2
                else:
                    # subtract from Barbara's score
                    Barbara -= int(record[i+1])

    # print the winner
    if Alice > Barbara:
        print('A')
    else:
        print('B')

if __name__ == '__main__':
    main()