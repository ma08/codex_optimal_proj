
import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b//gcd(a,b)

def main():
    input_lines = sys.stdin.readlines()
    num_clocks = int(input_lines[0])
    clock_times = [int(line) for line in input_lines[1:]]
    print(lcm(clock_times[0], clock_times[1]))

if __name__ == '__main__':
    main()
