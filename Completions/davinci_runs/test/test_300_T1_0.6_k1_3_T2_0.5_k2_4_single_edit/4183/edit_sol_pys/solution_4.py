
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a*b)//gcd(a, b)

def main():
    num_clocks = int(sys.stdin.readline().rstrip())
    for i in range(num_clocks):
        clock_times = int(sys.stdin.readline().rstrip())
        if i == 0:
            answer = clock_times
        else:
            answer = lcm(answer, clock_times)
    print(answer)

if __name__ == '__main__':
    main()
