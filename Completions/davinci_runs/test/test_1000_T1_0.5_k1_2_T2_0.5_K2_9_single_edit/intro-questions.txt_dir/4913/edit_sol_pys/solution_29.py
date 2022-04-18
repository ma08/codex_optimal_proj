

import sys

def main():
    # Read the input
    N = int(sys.stdin.readline())
    control = []
    vaccine = []
    for i in range(N):
        line = sys.stdin.readline().strip()
        if line[0] == 'Y':
            vaccine.append(line[1:])
        else:
            control.append(line[1:])
    
    # Find the number of infected people in the control and vaccine groups
    control_infections = [0, 0, 0]
    vaccine_infections = [0, 0, 0]
    for i in range(len(control)):
        for j in range(3):
            if control[i][j] == 'Y':
                control_infections[j] += 1
    for i in range(len(vaccine)):
        for j in range(3):
            if vaccine[i][j] == 'Y':
                vaccine_infections[j] += 1
    
    # Calculate the percentage of infected people in the control and vaccine groups
    control_percent = [x / float(len(control)) * 100 for x in control_infections]
    vaccine_percent = [x / float(len(vaccine)) * 100 for x in vaccine_infections]
    
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
