

import sys

def main():
    time_now = sys.stdin.readline()
    time_now = time_now.strip().split(":")
    time_now = [int(x) for x in time_now]

    time_explosion_in = sys.stdin.readline()
    time_explosion_in = time_explosion_in.strip().split(":")
    time_explosion_in = [int(x) for x in time_explosion_in]

    if time_explosion_in[0] < time_now[0]:
        time_explosion_in[0] += 24

    if time_explosion_in[1] < time_now[1]:
        time_explosion_in[0] -= 1
        time_explosion_in[1] += 60

    if time_explosion_in[2] < time_now[2]:
        time_explosion_in[0] -= 1
        time_explosion_in[1] -= 1
        time_explosion_in[2] += 60

    time_explosion_in = [str(x) for x in time_explosion_in]
    print(":".join(time_explosion_in))

main()
