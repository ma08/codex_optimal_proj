
import sys

def main():
    n = int(sys.stdin.readline())
    dirty_dishes = [int(x) for x in sys.stdin.readline().split()]
    current_dirtiness = 0
    cleanup_counter = 0
    for day in range(1, 366):
        if day in dirty_dishes:
            current_dirtiness += (day - dirty_dishes.index(day))
        else:
            current_dirtiness += 1
        if current_dirtiness >= 20:
            cleanup_counter += 1
            current_dirtiness = 0
    print(cleanup_counter)

if __name__ == '__main__':
    main()
