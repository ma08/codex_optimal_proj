

import sys

def main():
    time_now = [int(x) for x in sys.stdin.readline().strip().split(":")]
    time_explosion = [int(x) for x in sys.stdin.readline().strip().split(":")]

    time_explosion[0] += time_explosion[0] < time_now[0]
    time_explosion[1] += time_explosion[1] < time_now[1]
    time_explosion[2] += time_explosion[2] < time_now[2]

    time_explosion[1] += (time_explosion[2] - time_now[2]) // 60
    time_explosion[2] = (time_explosion[2] - time_now[2]) % 60

    time_explosion[0] += (time_explosion[1] - time_now[1]) // 60
    time_explosion[1] = (time_explosion[1] - time_now[1]) % 60

    print(":".join(map(str, time_explosion)))

main()
