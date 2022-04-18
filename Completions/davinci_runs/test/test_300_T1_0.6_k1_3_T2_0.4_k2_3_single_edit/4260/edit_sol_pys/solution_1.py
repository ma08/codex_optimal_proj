
import sys

def main():
    # read inputs
    inputs = sys.stdin.readlines()
    inputs = [input.rstrip().split() for input in inputs]

    # calculate time in world A
    for j in range(len(inputs)):
        T = float(inputs[j][0])
        X = float(inputs[j][1])
        print(T / X)

if __name__ == '__main__':
    main()
