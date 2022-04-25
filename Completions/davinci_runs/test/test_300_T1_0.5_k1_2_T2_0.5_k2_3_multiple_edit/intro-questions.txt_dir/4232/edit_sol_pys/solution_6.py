import sys

def main():
    n, m = input().strip().split()
    n = int(n) # number of people
    m = int(m) # number of people that have to be present
    numbers = [int(x) for x in input().strip().split()] # list of all the people present
    numbers.sort() # sort the list
    answer = 0 # the answer
    for i in range(n): # loop through the list
        if numbers[i] > answer + 1: # check if the next person is greater than the answer + 1, if it is, then break
            break # break
        if i + 1 >= m: # check if the number of people present is greater than or equal to the minimum number of people needed to be present
            answer = numbers[i] # set the answer to the current person
    if answer == 0: # check if the answer is 0
        print("-1") # if it is, then print -1
    else: # otherwise
        print(answer) # print the answer

if __name__ == "__main__":
    main()
