import sys

def main():
    time_now = [int(x) for x in sys.stdin.readline().strip().split(":")]

    time_explodes = [int(x) for x in sys.stdin.readline().strip().split(":")]

    if time_explodes[0] < time_now[0]:
        time_explodes[0] += 24

    if time_explodes[1] < time_now[1]:
        time_explodes[0] -= 1
        time_explodes[1] += 60

    if time_explodes[2] < time_now[2]:
        time_explodes[1] -= 1
        time_explodes[2] += 60

    time_explodes = [str(x) for x in time_explodes]
    print(":".join(time_explodes))

main()
