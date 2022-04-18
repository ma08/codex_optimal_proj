

import sys

def main():
    n = int(sys.stdin.readline())
    dirty_pushes = [int(x) for x in sys.stdin.readline().split()] #list of dirty pushes
    #print(n)
    #print(dirty_pushes)
    current_dirtiness = 0 #current dirtiness level
    cleanup_counter = 0
    for day in range(1, 366):
        if day in dirty_pushes: #if the day is in the list of dirty pushes
            current_dirtiness += (day - dirty_pushes.index(day)) #add the difference between the day and the index of the day in the dirty_pushes list
        else:
            current_dirtiness += 1 #otherwise, just add 1
        if current_dirtiness >= 20: #if the current dirtiness is greater than 20
            cleanup_counter += 1
            current_dirtiness = 0 #reset the current dirtiness to 0
    print(cleanup_counter)

if __name__ == '__main__':
    main()
