# https://open.kattis.com/problems/baconeggsandspam

import sys

def main():
    num_cases = int(sys.stdin.readline().strip())
    while num_cases != 0:
        num_cases -= 1

        num_orders = int(sys.stdin.readline().strip())
        orders = []
        for _ in range(num_orders):
            order = sys.stdin.readline().strip().split()
            orders.append(order)

    for brick in bricks[1:]:
        if brick > min_width:
            num_towers += 1
            min_width = brick

    print(num_towers)

if __name__ == '__main__':
    main()
