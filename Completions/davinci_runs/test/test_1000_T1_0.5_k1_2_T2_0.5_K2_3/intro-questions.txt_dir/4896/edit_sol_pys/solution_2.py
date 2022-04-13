# https://open.kattis.com/problems/baconeggsandspam

import sys

def main():
    num_cases = int(sys.stdin.readline().strip())

    for _ in range(num_cases):
        num_customers = int(sys.stdin.readline().strip())
        menu = {}

        for _ in range(num_customers):
            order = sys.stdin.readline().strip().split()
            name = order[0]

            for item in order[1:]:
                if item not in menu:
                    menu[item] = set()
                menu[item].add(name)

        sorted_items = sorted(menu.keys())

        for item in sorted_items:
            print(item + ' ' + ' '.join(sorted(menu[item])))

        print()

if __name__ == '__main__':
    main()
