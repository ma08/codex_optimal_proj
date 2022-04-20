

from sys import stdin

def main():
    n, m = [int(x) for x in stdin.readline().split()] # n = days, m = assignments
    assignments = [int(x) for x in stdin.readline().split()] # assignments = list of assignments
    assignments.sort() # sort assignments in ascending order
    assignments.reverse() # reverse assignments to descending order

    if sum(assignments) > n: # if the sum of assignments is greater than the days left, then we cannot finish the assignments
        print(-1)
        return

    days_left = n - sum(assignments) # days_left = days left after completing all assignments
    days_left += assignments.pop() # add the largest assignment to the days left
    days_left -= 1 # subtract 1 day for the largest assignment

    while days_left >= 0 and assignments: # while we have days left and assignments
        days_left -= assignments.pop() # subtract the next assignment from days left
        days_left -= 1 # subtract 1 day for the assignment

    if days_left < 0: # if days_left is less than 0, then we cannot finish the assignments
        print(-1)
    else:
        print(days_left) # print the days left

if __name__ == '__main__':
    main()
