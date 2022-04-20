
import sys

def is_all_bulbs_lighted(bulbs, switches, m):
    # Check if all bulbs are lighted
    for i in range(m):
        if bulbs[i] != switches[i]:
            return False, 0
    return True, 1

def count_switch_status(switches, n):
    count = 0
    for i in range(n):
        count += switches[i]
    return count

def light_bulb(bulbs, switches, switch_index):
    # Change the state of the bulb
    for i in range(len(bulbs[switch_index])):
        bulbs[switch_index][i] ^= 1

def main():
    # Get the number of switches and bulbs
    [n, m] = [int(s) for s in sys.stdin.readline().split()]
    n = int(n)
    m = int(m)
    # Get the state of each bulb
    bulbs = []
    for i in range(m):
        bulbs.append([int(s) for s in sys.stdin.readline().split()])
    # Get the switch that is connected to each bulb
    switches = [[] for i in range(n)]
    for i in range(m):
        [k, *switch_indexes] = [int(s) for s in sys.stdin.readline().split()]
        for j in range(k):
            switches[switch_indexes[j] - 1].append(i)
    # Calculate the minimum number of switches to be turned on
    count = 0
    switch_status = [0] * n
    while True:
        # Check if all bulbs are lighted
        all_bulbs_lighted, switch_count = is_all_bulbs_lighted(bulbs, switch_status, m)
        # If all bulbs are lighted, update the minimum number of switches that are turned on
        if all_bulbs_lighted:
            count = min(count, switch_count)
        # Increase the switch status
        switch_status[0] += 1
        for i in range(n - 1):
            if switch_status[i] == 2:
                switch_status[i] = 0
                switch_status[i + 1] += 1
        if switch_status[n - 1] == 2:
            break
    if count == n + 1:
        print('IMPOSSIBLE')
    else:
        print(count)

if __name__ == '__main__':
    main()
