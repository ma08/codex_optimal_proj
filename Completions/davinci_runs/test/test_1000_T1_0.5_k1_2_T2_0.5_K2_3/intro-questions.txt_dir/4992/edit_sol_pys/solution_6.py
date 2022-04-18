

import sys
import random

def check_safe(rooms, order):
    # check if the order is safe
    # if it is, return the order
    # if not, return None
    students = rooms[:] # copy the list
    pile = []
    for i in order:
        if i == 1:
            pile.extend(students[i-1]) # add the students to the pile
        else:
            if len(pile) < students[i-1]: # check if there is enough room
                return None
            else:
                pile.extend(students[i-1]) # add the students to the pile
    return order

def main(n, rooms):
    # generate all possible room orders
    # check if any are safe
    # if so, print one
    # if not, print "impossible"
    safe_order = None
    orders = []
    for i in range(1, n+1): # iterate through the possible first rooms
        for j in range(1, n+1): # iterate through the possible second rooms
            for k in range(1, n+1): # iterate through the possible third rooms
                for l in range(1, n+1): # iterate through the possible fourth rooms
                    order = [i, j, k, l] # create a new possible order
                    if len(set(order)) == n:
                        orders.append(order) # add the order to the list of possible orders
    random.shuffle(orders)
    for order in orders:
        if check_safe(rooms, order):
            safe_order = check_safe(rooms, order) # check if the order is safe
            break
    if safe_order: # if there is a safe order, print it
        print(' '.join(map(str, safe_order)))
    else: # otherwise, print impossible
        print('impossible')

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip()) # read the number of rooms
    rooms = [int(i) for i in sys.stdin.readline().strip().split()] # read the number of students in each room
    main(n, rooms)
