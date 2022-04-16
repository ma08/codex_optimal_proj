
import sys

def main():
    inputs = sys.stdin.readline().strip().split()
    inputs = [int(i) for i in inputs] #convert to int
    order = sys.stdin.readline().strip()
    inputs = sorted(inputs) #sort
    for i in order:
        print(inputs.pop(0), end=' ')

main()
