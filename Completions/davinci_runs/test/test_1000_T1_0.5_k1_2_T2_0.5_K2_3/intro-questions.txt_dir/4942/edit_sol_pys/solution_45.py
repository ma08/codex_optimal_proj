
import sys

def main():
    num_cases = int(sys.stdin.readline().strip())
    for case in range(num_cases):
        num_sticks = int(sys.stdin.readline().strip())
        stick_lengths = [int(x) for x in sys.stdin.readline().strip().split()]
        stick_lengths.sort()
        max_time = stick_lengths[-1]
        for i in range(len(stick_lengths)-2,-1,-1):
            max_time += 1 + stick_lengths[i]
        print(max_time)

if __name__ == '__main__':
    main()
