

import sys

def main():
    n = int(sys.stdin.readline())
    dirty_pushes = [int(x) for x in sys.stdin.readline().split()]
    #print(n)
    #print(dirty_pushes)
    current_dirtiness = 0
    cleanup_counter = 0
    for day in range(1, 366):
        if day in dirty_pushes.index(day):
            current_dirtiness += 1
        else:
            current_dirtiness += 1
        if current_dirtiness >= 20:
            cleanup_counter += 1
            current_dirtiness = 0
    print(cleanup_counter)

if __name__ == '__main__':
    main()
