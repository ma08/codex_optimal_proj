

import sys

def main():
    n = int(sys.stdin.readline())
    dirty_pushes = [int(x) for x in sys.stdin.readline().split()] # list of days when the button was pushed 
    #print(n)
    #print(dirty_pushes)
    current_dirtiness = 0 # number of days that have passed since the last time the button was pushed
    cleanup_counter = 0 # number of times the button was pushed
    for day in range(1, 366):
        if day in dirty_pushes: # if the button was pushed on this day
            current_dirtiness += (day - dirty_pushes.index(day))
        else: # if the button wasn't pushed on this day
            current_dirtiness += 1
        if current_dirtiness >= 20: # if the button was pushed 20 days ago
            cleanup_counter += 1
            current_dirtiness = 0
    print(cleanup_counter)

if __name__ == '__main__':
    main()
