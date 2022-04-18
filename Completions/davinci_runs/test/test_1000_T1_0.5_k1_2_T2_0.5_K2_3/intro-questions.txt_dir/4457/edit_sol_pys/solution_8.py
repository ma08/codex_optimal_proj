

import sys

def main():
    cans = int(sys.stdin.readline()) # cans to shoot
    duras = [int(x) for x in sys.stdin.readline().split()] # durations
    shot = 0 # total time
    shotList = [] # list of cans in order of duration
    for i in range(cans): # add cans to list
        shotList.append(i+1) # add can to list
    shotList.sort(key=lambda x: duras[x-1]) # sort cans by duration
    for i in range(cans): # iterate through cans by duration
        shot += (duras[shotList[i]-1]*i+1) # add time to total
    print(shot) # print time
    print(*shotList) # print cans

if __name__ == "__main__":
    main()
