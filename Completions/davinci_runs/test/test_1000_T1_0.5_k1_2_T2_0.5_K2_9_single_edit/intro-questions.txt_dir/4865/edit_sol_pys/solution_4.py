import sys
def main():
    num_cases = int(sys.stdin.readline())
    for i in range(num_cases):
        line = sys.stdin.readline().strip()
        if line == "F":
            line = sys.stdin.readline().strip().split()
            minutes = int(line[0])
            hours = int(line[1])
            min_of_day = int(line[2])
            if min_of_day + minutes >= 60:
                hours += 1 
                min_of_day = (min_of_day + minutes) % 60 
            else:
                min_of_day += minutes
            if hours == 24:
                hours = 0
            print(hours, min_of_day)
        elif line == "B":
            line = sys.stdin.readline().strip().split()
            minutes = int(line[0])
            hours = int(line[1])
            min_of_day = int(line[2])
            if min_of_day - minutes < 0:
                hours -= 1
                min_of_day = 60 + (min_of_day - minutes)
            else:
                min_of_day -= minutes
            if hours == -1:
                hours = 23
            print(hours, min_of_day)
main()
