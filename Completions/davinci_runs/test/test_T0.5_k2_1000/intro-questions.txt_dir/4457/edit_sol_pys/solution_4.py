
import sys

def main():
    cans = int(sys.stdin.readline()) # number of cans
    duras = [int(x) for x in sys.stdin.readline().split()] # list of durations
    shot = 0 # total time
    shotList = [] # list of cans to be shot
    for i in range(cans): # fill shotList with all the cans
        shotList.append(i+1) 
    shotList.sort(key=lambda x: duras[x-1]) # sort shotList by duration 
    for i in range(cans): # add the time to shot
        shot += (duras[shotList[i]-1]*i+1) 
    print(shot) # print the total time
    print(*shotList) # print the shotList

if __name__ == "__main__":
    main()
