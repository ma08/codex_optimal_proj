

import sys
import random

def check_safe(rooms, order):
    # Check if the order is safe
    # If it is, return the order
    # If not, return None
    students = rooms[:]
    pile = []
    for i in order:
        if i == 1:
            pile.extend(rooms[0])
        else:
            if len(pile) < rooms[i-1] - 1:
                return None
            else:
                pile.extend(rooms[i-1] - 1)
    return order

def main(n, rooms):
    # Generate all possible room orders
    # Check if any are safe
    # If so, print one
    # If not, print "impossible"
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
