

from sys import stdin

def main():
    n, m = [int(x) for x in stdin.readline().split()] # n is the number of days left, m is the number of assignments
    assignments = [int(x) for x in stdin.readline().split()] # list of assignments
    assignments.sort() # sort the assignments in ascending order
    assignments.reverse() # reverse the list

    if sum(assignments) > n: # if the sum of assignments is greater than the number of days left, then there is no way to finish all assignments
        print(-1)
        return

    days_left = n - sum(assignments) # the number of days left after finishing all assignments
    days_left += assignments.pop() # add the last assignment to the days left
    days_left -= 1 # subtract 1 day to account for the last assignment

    while days_left >= 0 and assignments: # while there are still days left and assignments
        days_left -= assignments.pop() # subtract the assignment from the days left
        days_left -= 1 # subtract 1 day to account for the assignment

    if days_left < 0: # if there are no days left, then there is no way to finish all assignments
        print(-1)
    else:
        print(days_left)

if __name__ == '__main__':
    main()
