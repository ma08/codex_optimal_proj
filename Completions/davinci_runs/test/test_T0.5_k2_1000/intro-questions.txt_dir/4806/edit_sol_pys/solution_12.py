
def mech_monster(monster_moves):
    mech_moves = ""
    combo_breaker_queue = []
    for move in monster_moves:
        if move == 'R':
            mech_moves += 'S'
        elif move == 'B':
            mech_moves += 'K'
        elif move == 'L':
            mech_moves += 'H'
        if len(combo_breaker_queue) == 3:
            combo_breaker_queue.pop(0)
        combo_breaker_queue.append(move)
        if len(combo_breaker_queue) == 3 and \
           combo_breaker_queue[0] != combo_breaker_queue[1] and \
           combo_breaker_queue[1] != combo_breaker_queue[2] and \
           combo_breaker_queue[0] != combo_breaker_queue[2]:
            mech_moves += 'C'
    return mech_moves

def main():
    print(mech_monster('RBL'))

if __name__ == '__main__':
    main()
