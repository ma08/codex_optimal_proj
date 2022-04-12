import sys

def main():
    n = int(sys.stdin.readline().strip())
    temp = [int(i) for i in sys.stdin.readline().strip().split()] # readline() returns a string, so we need to convert it to int
    max_temp = [] # store the maximum temperature of each 3-day period
    for i in range(len(temp)-2): # we only need to consider the first n-2 days
        max_temp.append(max(temp[i], temp[i+1], temp[i+2])) # append the maximum temperature of each 3-day period to the list
    index = max_temp.index(min(max_temp)) # find the index of the minimum maximum temperature
    print(index+1, max_temp[index]) # print the index of the minimum maximum temperature and the minimum maximum temperature

if __name__ == '__main__':
    main()
