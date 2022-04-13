

import sys

def main():
    n = int(sys.stdin.readline())
    days = [int(x) for x in sys.stdin.readline().split()]
    days.append(366) # to make the loop work
    curr_day = 1
    clean_ups = 0
    for i in range(n):
        while days[i] >= curr_day:
            if days[i] - curr_day > 20:
                clean_ups += 1
                curr_day = days[i] + 1
            else:
                curr_day = days[i] + 1
                break
    print(clean_ups)

if __name__ == "__main__":
    main()
