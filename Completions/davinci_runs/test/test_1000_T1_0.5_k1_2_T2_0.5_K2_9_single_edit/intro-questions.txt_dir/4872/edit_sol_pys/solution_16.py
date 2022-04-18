

import sys

def main():
    n = int(sys.stdin.readline())
    days = [int(x) for x in sys.stdin.readline().split()]
    days.append(366)
    curr_day = 1
    ans = 0
    cleanups = 0
    for i in range(n):
        while curr_day < days[i + 1]:
            if days[i + 1] - curr_day > 20:
                cleanups += 1
                curr_day = days[i + 1] + 1
            else:
                curr_day = days[i + 1] + 1
                break
    ans = cleanups
    print(ans)

if __name__ == "__main__":
    main()
