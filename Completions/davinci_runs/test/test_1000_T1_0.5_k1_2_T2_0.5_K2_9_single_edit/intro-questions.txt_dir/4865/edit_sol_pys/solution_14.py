import sys

def main():
    num_cases = int(sys.stdin.readline())
    for i in range(num_cases):
        line = sys.stdin.readline().split()
        direction = line[0]
        minutes = int(line[1])
        hours = int(line[2])
        min_of_day = int(line[3])
        if direction == "F":
            if min_of_day + minutes >= 60:
                hours += 1
                min_of_day = (min_of_day + minutes) % 60
            else:
                min_of_day += minutes
            if hours == 24:
                hours = 0
            print(hours, min_of_day, sep=' ')
        else:
            if min_of_day - minutes < 0:
                hours -= 1
                min_of_day = 60 + (min_of_day - minutes)
            else:
                min_of_day -= minutes
            if hours == -1:
                hours = 23
            print(hours, min_of_day, sep=' ')
main()
