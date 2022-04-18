

import sys

def main():
    n = int(sys.stdin.readline().strip())
    values = [int(x) for x in sys.stdin.readline().strip().split()]
    values = values[::-1]
    differences = []
    for i in range(len(values) - 1):
        differences.append(values[i] - values[i + 1])
    differences.append(values[-1])
    differences = differences[::-1]
    
    # find the degree of the polynomials
    degree = 0
    for i in range(len(differences) - 1):
        if differences[i] != differences[i + 1]:
            degree = i + 1
            break
    
    # find the next values
    next_value = values[0] + (degree + 1) * differences[degree]
    
    print(degree, next_value)

if __name__ == '__main__':
    main()
