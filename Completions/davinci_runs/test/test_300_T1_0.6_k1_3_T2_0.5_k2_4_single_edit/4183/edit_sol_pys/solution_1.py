

import sys

def main():
    input = sys.stdin.readline().rstrip()
    num_clocks = int(input)
    clock_times = []
    for clock in range(num_clocks):
        clock_times.append(int(input))

    answer = clock_times[0]
    for clock in clock_times[1:]:
        answer = lcm(answer, clock)
    print(answer)

if __name__ == '__main__':
    main()
