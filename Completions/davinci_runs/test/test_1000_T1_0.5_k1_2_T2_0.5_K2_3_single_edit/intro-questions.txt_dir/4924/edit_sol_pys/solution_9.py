

import sys

def main():
    time_now = sys.stdin.readline().strip().split(":")
    time_now = [int(x) for x in time_now] # convert to int

    time_explosion = sys.stdin.readline().strip().split(":")
    time_explosion = [int(x) for x in time_explosion] # convert to int

    if time_explosion[0] < time_now[0]:
        time_explosion[0] += 24

    if time_explosion[1] < time_now[1]:
        time_explosion[0] -= 1
        time_explosion[1] += 60

    if time_explosion[2] < time_now[2]:
        time_explosion[1] -= 1
        time_explosion[2] += 60

    time_explosion = [str(x) for x in time_explosion] # convert to str
    print(":".join(time_explosion))

main()
