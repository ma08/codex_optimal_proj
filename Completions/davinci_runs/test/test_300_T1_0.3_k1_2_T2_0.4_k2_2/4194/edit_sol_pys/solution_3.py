

from sys import stdin

def main():
    n, m = [int(x) for x in stdin.readline().split()] # n = days, m = assignments
    assignments = [int(x) for x in stdin.readline().split()] # assignments
    assignments.sort() # sort assignments
    assignments.reverse() # reverse assignments

    if sum(assignments) > n: # if the sum of the assignments is more than the days
        print(-1)
        return

    days_left = n - sum(assignments) # days left
    days_left += assignments.pop() # add the last assignment
    days_left -= 1 # subtract 1

    while days_left >= 0 and assignments: # while days left is greater than 0 and there are assignments
        days_left -= assignments.pop()
        days_left -= 1

    if days_left < 0: # if days left is less than 0
        print(-1)
    else: # else
        print(days_left)

if __name__ == '__main__':
    main()
