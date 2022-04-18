
import sys

def main():
    n = int(sys.stdin.readline())
    days = [int(x) for x in sys.stdin.readline().split()]
    days.append(367)
    curr_day = 1
    cleanups = 1
    for i in range(n):
        if days[i] - curr_day > 20:
            cleanups += 1
            curr_day = days[i] + 1
        else:
            curr_day = days[i] + 1
    print(cleanups)

if __name__ == "__main__":
    main()
