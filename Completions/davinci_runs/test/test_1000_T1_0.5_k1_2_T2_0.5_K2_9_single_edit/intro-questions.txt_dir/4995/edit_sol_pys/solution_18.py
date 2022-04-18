

import sys

# define function
def avg_min(n, M, S, C):
    # initialize variables
    sum_min = 0
    avg = 0
    # loop through all the observations
    for i in range(n):
        # convert the seconds to minutes
        sum_min += S[i]/60
        # calculate the average
        avg = sum_min/C[i]
    # check if the average is less than a minute
    if avg <= 1:
        return "measurement error"
    else:
        return avg

# define main function
def main():
    # get the number of observations
    n = int(sys.stdin.readline().strip())
    # initialize variables
    M = []
    S = []
    C = []
    # loop through all the observations
    for i in range(n):
        # get the minutes and seconds
        m, s, c = map(int, sys.stdin.readline().strip().split())
        # add the minutes to the list
        M.append(m)
        # add the seconds to the list
        S.append(s)
        # add the number of cycles to the list
        C.append(c)
    # print the average length of an SL minute
    print(avg_min(n, M, S, C))

# run main function
if __name__ == "__main__":
    main()
