
import sys

def main():
    n = int(sys.stdin.readline())
    dirty_pushes = [int(x) for x in sys.stdin.readline().split()] #this is a list comprehension
    current_dirtiness = 0
    cleanup_counter = 0
    for day in range(1, 366): #this is a range from 1 to 365
        if day in dirty_pushes:
            current_dirtiness += (day - dirty_pushes.index(day))
        else:
            current_dirtiness += 1
        if current_dirtiness >= 20: #this is a comparison
            cleanup_counter += 1
            current_dirtiness = 0
    print(cleanup_counter)

if __name__ == '__main__':
    main()
