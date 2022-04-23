
from sys import stdin

def main():
    n = int(stdin.readline().strip())
    skill_list = [int(x) for x in stdin.readline().strip().split()]
    min_skill = min(skill_list) - 1

    # create a list of tuples of each skill and the number of students
    # with that skill level
    skill_counts = {}
    for i in range(min_skill, max(skill_list) + 1):
        skill_counts[i] = skill_list.count(i)

    # sort the skill counts by the number of students with that skill level
    skill_counts = sorted(skill_counts.items(), key=lambda x: x[1])

    # find the minimum number of students needed to form a team
    # of each skill level
    min_students = 0
    for skill, count in skill_counts:
        if count < n:
            min_students += (n - count) * skill
            n = count * skill
        else:
            min_students += n * skill
            break

    print(min_students)

main()
