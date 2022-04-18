# coding=utf-8

import sys

def main():
    num_participants, budget, num_hotels, num_weeks = map(int, sys.stdin.readline().split())
    for h in range(num_hotels):
        price = int(sys.stdin.readline())
        beds = map(int, sys.stdin.readline().split())
        for w in range(num_weeks):
            if beds[w] >= num_participants and price * num_participants <= budget:
                print price * num_participants
                return
    print "stay home"

if __name__ == "__main__":
    main()
