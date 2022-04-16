
import sys

def main():
    num_players = int(sys.stdin.readline())
    players = []
    for i in range(num_players):
        players.append(sys.stdin.readline().rstrip())
    if sorted(players) == players and len(players) > 1:
        print('INCREASING')
    elif sorted(players, reverse=True) == players and len(players) > 1:
        print('DECREASING')
    else:
        print('NEITHER')

if __name__ == '__main__':
    main()
