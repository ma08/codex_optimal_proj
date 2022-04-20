

import sys

def main():
    num_students = int(sys.stdin.readline())
    skills = [int(x) for x in sys.stdin.readline().split()]
    skills.sort()

    i = 0
    j = 0
    max_team_size = 0
    while i < num_students:
        while j < num_students and skills[j] - skills[i] <= 5:
            j += 1
        max_team_size = max(max_team_size, j - i)
        i += 1

    print(max_team_size)

if __name__ == '__main__':
    main()