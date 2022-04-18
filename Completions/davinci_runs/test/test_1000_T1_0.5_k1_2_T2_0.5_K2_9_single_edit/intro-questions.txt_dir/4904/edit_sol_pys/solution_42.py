

import sys

def main():
    game = sys.stdin.readline().strip()


    alice = 0

    barbara = 0


    for i in range(0, len(game), 2):

        if game[i] == 'A':

            alice += int(game[i + 1])

            if alice >= 11 and alice - barbara >= 2:
                print('A')
                break

        else:

            barbara += int(game[i + 1])

            if barbara >= 11 and barbara - alice >= 2:
                print('B')
                break


if __name__ == '__main__':
    main()
