
# 
import sys

def main():
    n = int(sys.stdin.readline())
    days = [int(x) for x in sys.stdin.readline().split()]
    days.append(366)
    curr_day = 1
    cleanups = 0
    for i in range(n):
        while days[i] >= curr_day:
            if days[i] - curr_day > 20:
                cleanups += 1
                curr_day = days[i] + 1
            else:
                curr_day = days[i] + 1
                break
    print(cleanups)

if __name__ == "__main__":
    main()
