

import sys

def main():
    n = int(sys.stdin.readline())
    dirty_pushes = [int(x) for x in sys.stdin.readline().split()] # list of days when the button was pushed 
    #print(n)
    #print(dirty_pushes)
    current_dirtiness = 0 # current dirtiness of the button
    cleanup_counter = 0
    for day in range(1, 366):
        if day in dirty_pushes: # if the button was pushed today
            current_dirtiness += (day - dirty_pushes.index(day))
        else: # if the button was not pushed today
            current_dirtiness += 1
        if current_dirtiness >= 20: # if the button is too dirty
            cleanup_counter += 1
            current_dirtiness = 0
    print(cleanup_counter)

if __name__ == '__main__':
    main()
