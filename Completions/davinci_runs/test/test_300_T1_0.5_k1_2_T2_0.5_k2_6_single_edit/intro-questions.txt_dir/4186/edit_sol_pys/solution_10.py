

from sys import stdin

def main():
    n = int(input())
    skill_list = [int(x) for x in input().split()]
    min_skill = min(skills)

    # create a list of tuples of each skill and the number of students
    # with that skill
    skill_counts = []
    for i in range(min_skill, max(skills) + 1):
        skill_counts.append((i, skills.count(i)))

    # sort the skill counts by the number of students with that skill
    skill_counts.sort(key=lambda x: x[1])

    # find the minimum number of students needed to form a team
    # of each skill level
    min_students = 0
    for i, count in skill_counts:
        if count <= n:
            min_students += (n - count)
            n = count
        else:
            min_students += n
            break

    print(min_students)

main()
