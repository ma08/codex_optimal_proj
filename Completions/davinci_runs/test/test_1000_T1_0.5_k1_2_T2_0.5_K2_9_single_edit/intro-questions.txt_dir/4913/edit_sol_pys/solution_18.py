

import sys

def main():
    # Read the input
    N = int(sys.stdin.readline())
    control = [0, 0, 0]
    vaccine = [0, 0, 0]
    for i in range(N):
        line = sys.stdin.readline().strip()
        if line[0] == 'Y':
            for j in range(3):
                if line[j + 1] == 'Y':
                    vaccine[j] += 1
        else:
            for j in range(3):
                if line[j + 1] == 'Y':
                    control[j] += 1
    
    # Find the number of infected people in the control and vaccine groups

    # Calculate the percentage of infected people in the control and vaccine groups
    control_percent = [x / N * 100 for x in control]
    vaccine_percent = [x / N * 100 for x in vaccine]
    
    # Calculate the efficacy
    efficacy = [0, 0, 0]
    for i in range(3):
        if control_percent[i] == 0:
            efficacy[i] = 'Not Effective'
        else:
            efficacy[i] = 100 - vaccine_percent[i] / control_percent[i] * 100
    
    # Output the result
    for i in range(3):
        print(efficacy[i])

if __name__ == '__main__':
    main()
