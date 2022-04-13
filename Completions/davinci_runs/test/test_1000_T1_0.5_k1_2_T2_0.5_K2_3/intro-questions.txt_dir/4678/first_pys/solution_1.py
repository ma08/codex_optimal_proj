

import sys

def main():
    num_people = int(sys.stdin.readline())
    heights = [int(x) for x in sys.stdin.readline().split()]
    stools = [0 for i in range(num_people)]
    current_max = 0
    for i in range(num_people):
        stools[i] = max(current_max, heights[i])
        current_max = stools[i]
    print(sum(stools))

main()