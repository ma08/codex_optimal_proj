

import sys, math

def get_input():
    numDays = int(sys.stdin.readline())
    temp = sys.stdin.readline().split()
    temp = [int(i) for i in temp]
    return numDays, temp

def main():
    numDays, temp = get_input()
    minTemp = 100
    minDay = 0
    for i in range(0,numDays-2):
        if temp[i]+temp[i+1]+temp[i+2] < minTemp:
            minTemp = temp[i]+temp[i+1]+temp[i+2]
            minDay = i+1

    print(minDay, minTemp)

if __name__=="__main__":
    main()
