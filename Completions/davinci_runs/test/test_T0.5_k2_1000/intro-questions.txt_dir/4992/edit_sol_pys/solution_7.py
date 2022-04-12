

import sys
import random

def check_safe(rooms, order, n):
    # Check if the order is safe. If it is, return the order. If not, return None.
    for i in range(n):
        if order[i] == 1:
            pile = rooms[i]
        else:
            if len(pile) < rooms[i]:
                return False
            pile += rooms[i]
    return True

def main(n, rooms):
    # Generate all possible room orders.
    # Check if any are safe.
    # If so, print one.
    # If not, print "impossible".
    safe_order = None
    orders = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                for l in range(1, n+1):
                    order = [i, j, k, l]
                    if len(set(order)) == n:
                        orders.append(order)
    random.shuffle(orders)
    for order in orders:
        if check_safe(rooms, order):
            safe_order = check_safe(rooms, order)
            break
    if safe_order:
        print(' '.join(map(str, safe_order)))
    else:
        print('impossible')

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    rooms = [int(i) for i in sys.stdin.readline().strip().split()]
    main(n, rooms)
