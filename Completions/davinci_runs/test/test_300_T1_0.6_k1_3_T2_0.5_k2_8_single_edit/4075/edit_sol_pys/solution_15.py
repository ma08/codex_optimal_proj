
import sys

def is_all_bulbs_lighted(bulbs, switches):
    for bulb in bulbs:
        bulb_switch_count = 0
        # On/Off state of switches that are connected to the bulb
        for switch in bulb['switches']:
            bulb_switch_count += switches[switch - 1]
        # If the count is not congruent to p mod 2, the bulb is not lit
        if bulb_switch_count % 2 != bulb['p']:
            return False
    return True
def print_switch_status(bulbs, switches):
    switch_status = []
    for i in range(len(switches)):
        switch_status.append('on' if switches[i] == 1 else 'off')
    print(switch_status)
def main():
    # Get the number of switches and bulbs
    [n, m] = sys.stdin.readline().split()
    n = int(n)
    m = int(m)
    # Get the connected switches and p for each bulb
    bulbs = []
    for i in range(m):
        # Get the number of switches that are connected to the bulb
        k = int(sys.stdin.readline().split()[0])
        # Get the connected switches
        switches = [int(s) for s in sys.stdin.readline().split()]
        # Get p
        p = int(sys.stdin.readline().split()[0])
        bulbs.append({'switches': switches, 'p': p})
    # Calculate the number of combinations of "on" and "off" states of the switches that light all the bulbs
    count = 0
    switches = [0] * n
    while True:
        if is_all_bulbs_lighted(bulbs, switches):
            # print_switch_status(bulbs, switches)
            count += 1
        # Increase the switch count
        switches[0] += 1
        for i in range(n - 1):
            if switches[i] == 2:
                switches[i] = 0
                switches[i + 1] += 1
        if switches[n - 1] == 2:
            break
    print(count)

if __name__ == '__main__':
    main()
