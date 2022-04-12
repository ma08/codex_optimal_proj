
import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp = [int(i) for i in sys.stdin.readline().strip().split()] # read in an array of integers
    max_temp = []
    for i in range(len(temp)-2): # loop through the array
        max_temp.append(max(temp[i], temp[i+1], temp[i+2])) # add the max of 3 consecutive elements to max_temp
    index = max_temp.index(min(max_temp)) # find the index of the minimum max
    print(index+1, max_temp[index])

if __name__ == '__main__':
    main()
