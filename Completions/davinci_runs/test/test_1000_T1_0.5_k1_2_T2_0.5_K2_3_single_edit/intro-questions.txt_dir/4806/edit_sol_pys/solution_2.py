
#This solution is O(n) in time and O(n) in space
def mech_monster(monster_moves):
    mech_moves = ""
    move_queue = []
    for move in monster_moves:
        if move == 'R':
            mech_moves += 'S'
        elif move == 'B':
            mech_moves += 'K'
        elif move == 'L':
            mech_moves += 'H'
        if len(move_queue) == 3:
            move_queue.pop(0)
        move_queue.append(move)
        if len(move_queue) == 3 and \
           move_queue[0] != move_queue[1] and \
           move_queue[1] != move_queue[2] and \
           move_queue[0] != move_queue[2]:
            mech_moves += 'C'
    return mech_moves

#This solution is O(n) in time and O(1) in space
def mech_monster(monster_moves):
    mech_moves = ""
    move_counts = {'R': 0, 'B': 0, 'L': 0}
    for move in monster_moves:
        if move == 'R':
            mech_moves += 'S'
            move_counts['R'] += 1
        elif move == 'B':
            mech_moves += 'K'
            move_counts['B'] += 1
        elif move == 'L':
            mech_moves += 'H'
            move_counts['L'] += 1
        if move_counts['R'] == 1 and \
           move_counts['B'] == 1 and \
           move_counts['L'] == 1:
            mech_moves += 'C'
            move_counts = {'R': 0, 'B': 0, 'L': 0}
    return mech_moves

import sys
def main():
    monster_moves = sys.stdin.readline().strip()
    print(mech_monster(monster_moves))

if __name__ == '__main__':
    main()
