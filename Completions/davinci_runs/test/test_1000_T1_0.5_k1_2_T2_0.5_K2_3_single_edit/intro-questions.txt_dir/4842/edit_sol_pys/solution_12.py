
import sys

def main():
    n = int(input())
    values = [int(x) for x in input().strip().split()]
    differences = [values[i] - values[i - 1] for i in range(1, len(values))]
    
    degree = len(differences) - 1
    while differences[degree - 1] == differences[degree]:
        degree -= 1
    
    # find the next value
    next_value = values[-1] + (degree + 1) * differences[degree]
    
    print(degree, next_value)

if __name__ == '__main__':
    main()
