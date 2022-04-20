
from sys import stdin

def main():
    n, m = [int(x) for x in stdin.readline().split()]
    assignments = [int(x) for x in stdin.readline().split()]
    assignments.sort()
    assignments.reverse()

    if sum(assignments) > n:
        print(-1)
        return

    days_left = n - sum(assignments)
    days_left += assignments.pop()
    days_left -= 1

    while days_left >= 0 and assignments:
        days_left -= assignments.pop()
        days_left -= 1

    if days_left < 0:
        print(-1)
    else:
        print(days_left)

if __name__ == '__main__':
    main()
