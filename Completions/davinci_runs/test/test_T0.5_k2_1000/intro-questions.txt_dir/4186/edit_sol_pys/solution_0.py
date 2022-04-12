

from sys import stdin

def main():
    n = int(stdin.readline())
    skill_list = [int(x) for x in stdin.readline().split()] # list comprehension
    min_skill = min(skill_list)

    # create a list of tuples of each skill and the number of students
    # with that skill
    skill_counts = []
    for i in range(min_skill, max(skill_list) + 1):
        skill_counts.append((i, skill_list.count(i)))

    # sort the skill counts by the number of students with that skill level
    skill_counts.sort(key=lambda x: x[1]) # lambda function

    # find the minimum number of students needed to form teams
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
