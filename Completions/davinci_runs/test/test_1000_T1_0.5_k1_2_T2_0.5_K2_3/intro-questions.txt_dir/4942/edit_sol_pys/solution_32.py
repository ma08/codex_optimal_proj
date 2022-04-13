

import sys

def main():
    num_soldiers = int(sys.stdin.readline().strip()) # read the number of soldiers
    soldier_growth_times = [int(x) for x in sys.stdin.readline().strip().split()] # read the time it takes for each soldier to grow
    soldier_growth_times.sort() # sort the soldier growth times
    max_time = soldier_growth_times[-1] # the maximum time will be the time of the last soldier
    for i in range(len(soldier_growth_times)-2,-1,-1): # for each soldier before the last one
        max_time += 1 + soldier_growth_times[i] # add one to the maximum time and then add the time it takes for that soldier to grow
    print(max_time) # print the maximum time

if __name__ == '__main__':
    main()
