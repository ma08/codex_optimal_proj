import sys


def main():
    num_cases = int(sys.stdin.readline())
    for i in range(num_cases):
        direction, minutes, hours, min_of_day = sys.stdin.readline().split()
        minutes = int(minutes)
        hours = int(hours)
        min_of_day = int(min_of_day)
        if direction == "F":
            if min_of_day + minutes >= 60:
                hours += 1
                min_of_day = (min_of_day + minutes) % 60
            else:
                min_of_day += minutes
            if hours == 24:
                hours = 0
            print(hours, min_of_day, sep=" ")
        else:
            if min_of_day - minutes < 0:
                hours -= 1
                min_of_day = 60 + (min_of_day - minutes)
            else:
                min_of_day -= minutes
            if hours == -1:
                hours = 23
            print(hours, min_of_day, sep=" ")
main()
