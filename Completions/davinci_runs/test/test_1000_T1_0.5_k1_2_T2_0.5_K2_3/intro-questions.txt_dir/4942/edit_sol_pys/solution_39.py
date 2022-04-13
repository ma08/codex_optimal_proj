

import sys

def main():
    num_sticks = int(sys.stdin.readline().strip())
    stick_lengths = [int(x) for x in sys.stdin.readline().strip().split()]
    stick_lengths.sort()
    max_time = stick_lengths[-1]
    for i in range(len(stick_lengths)-2, -1, -1):
        max_time += stick_lengths[i] + 1
    print(max_time)

if __name__ == '__main__':
    main()
