

import sys

def main():
    time_now = sys.stdin.readline()
    time_now = time_now.strip().split(":")
    time_now = [int(x) for x in time_now]

    time_explode = sys.stdin.readline()
    time_explode = time_explode.strip().split(":")
    time_explode = [int(x) for x in time_explode]

    if time_explode[0] < time_now[0]:
        time_explode[0] += 24

    if time_explode[1] < time_now[1]:
        time_explode[0] -= 1
        time_explode[1] += 60

    if time_explode[2] < time_now[2]:
        time_explode[1] -= 1
        time_explode[2] += 60

    time_explosion = [str(x) for x in time_explosion]
    print(":".join(time_explosion))

main()
