
import sys

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a 
def lcm(a,b):
    return a*b//gcd(a,b)

def main():
    num_clocks = int(sys.stdin.readline().strip())
    clock_times = list(map(int,sys.stdin.readline().strip().split()))
    lcm_value = clock_times[0]
    for clock in clock_times[1:]:
        lcm_value = lcm(lcm_value,clock)
    print(lcm_value)

if __name__ == '__main__':
    main()
