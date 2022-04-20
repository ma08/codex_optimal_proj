
import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b/gcd(a, b)

def main():
    num_clocks = int(sys.stdin.readline().rstrip())
    clock_times = []
    for clock in range(num_clocks):
        clock_times.append(int(sys.stdin.readline().rstrip()))
    answer = clock_times[0]
    for clock in clock_times[1:]:
        answer = lcm(answer, clock)
    print(answer)

if __name__ == '__main__':
    main()
