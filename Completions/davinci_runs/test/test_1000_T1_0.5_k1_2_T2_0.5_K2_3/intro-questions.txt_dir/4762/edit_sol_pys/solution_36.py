
import sys
from math import factorial

def main():
    N = int(sys.stdin.readline().strip())
    print(round(sum([((-1)**(i+1)) * factorial(N) / (factorial(i) * factorial(N-i)) for i in range(1, N+1)]) / N, 8), end='')

main()
