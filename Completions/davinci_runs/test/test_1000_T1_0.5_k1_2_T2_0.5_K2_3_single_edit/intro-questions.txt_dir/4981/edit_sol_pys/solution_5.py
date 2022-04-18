

import sys

def main():
    inputs = sys.stdin.readline().strip().split()
    inputs = [float(i) for i in inputs]
    order = sys.stdin.readline().strip()
    inputs = sorted(inputs)
    for i in order:
        print(inputs.pop(0), end=' ')

main()
