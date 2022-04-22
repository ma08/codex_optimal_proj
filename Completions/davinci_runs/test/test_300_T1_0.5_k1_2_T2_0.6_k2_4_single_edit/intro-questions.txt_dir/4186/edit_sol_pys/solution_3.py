

from sys import stdin

def main():
    n = int(stdin.readline())
    skill_list = [int(x) for x in stdin.readline().split()]
    min_skill = min(skill_list)

    # create a list of tuples of each skill and the number of students
    # with that skill
    skill_counts = []
    for i in range(min_skill, max(skill_list)):
        skill_counts.append((i, skill_list.count(i)))

    # sort the skill counts by the number of students with that skill
    skill_counts.sort(key=lambda x: x[1])

    # find the minimum number of students needed to form a team
    # of each skill level
    min_students = 0
    for skill, count in skill_counts:
        if count <= n: # if there aren't enough students with this skill,
                       # then we need to add n-count students of the skill
            min_students += (n - count) 
            n = count # update the number of students needed
        else:
            min_students += n # otherwise, we only need to add n students of the skill
            break

    print(min_students)

main()
