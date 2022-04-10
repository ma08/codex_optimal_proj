

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    skills = sorted(map(int, sys.stdin.readline().split()))

    # If we have less teams than students, then we can't have a team with more than 1 student.
    # So, the answer is the number of students.
    if k < n:
        print(n)
        return

    # If the difference between the highest and lowest skill is less than 5, then
    # the answer is the number of students.
    if skills[-1] - skills[0] < 5:
        print(n)
        return

    # If the difference between the highest and lowest skill is more than 5, then
    # the answer is the number of teams.
    if skills[-1] - skills[0] > 5:
        print(k)
        return

    # If we have the same number of teams as students, then we can have a team with all
    # students. So, the answer is the number of students.
    if n == k:
        print(n)
        return

    # Otherwise, we have to find the maximum number of teams we can have, such that
    # the difference between the highest and lowest skill is less than 5.
    #
    # To do this, we start from the smallest skill and find the number of teams we can
    # have with this skill as the lowest skill. Then, we try the next-highest skill
    # and find the number of teams we can have with this skill as the lowest skill.
    # We repeat this until the difference between the lowest skill and the highest
    # skill is 5.
    #
    # We keep track of the maximum number of teams we can have.
    max_teams = 0
    i = 0
    while i < n:
        num_teams = 1
        j = i + 1
        while j < n and skills[j] - skills[i] <= 5:
            num_teams += 1
            j += 1
        if num_teams > max_teams:
            max_teams = num_teams
        i += 1

    print(max_teams)

if __name__ == "__main__":
    main()