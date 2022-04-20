

import math

def main():
    a, b, c = map(int, input().split())
    days = [a, b, c]
    days.sort()
    days_eaten = 0
    for i in range(3):
        days_eaten += math.floor(days[i]/3)
        days[i] -= math.floor(days[i]/3)*3
    days.sort()
    if days[0] == 0:
        days_eaten += days[1]+days[2]
    else:
        days_eaten += days[0] + math.floor((days[1]+days[2]-days[0])/2)
    print(days_eaten)

if __name__ == "__main__":
    main()