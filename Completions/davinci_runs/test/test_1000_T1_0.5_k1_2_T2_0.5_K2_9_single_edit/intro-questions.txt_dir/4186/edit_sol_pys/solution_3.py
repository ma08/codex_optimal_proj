

from sys import stdin

def main():
    n = int(stdin.readline()) # number of students
    skill_list = [int(x) for x in stdin.readline().split()] # students' skills
    min_skill = min(skill_list) # minimum skill level

    # create a list of tuples of each skill and the number of students
    # with that skill
    skill_counts = []
    for i in range(min_skill, max(skill_list) + 1): # include max skill
        skill_counts.append((i, skill_list.count(i)))

    # sort the skill counts by the number of students with that skill
    skill_counts.sort(key=lambda x: x[1])

    # find the minimum number of students needed to form a team
    # of each skill level
    min_students = 0 # number of students needed to form teams
    for i, count in skill_counts:
        if count <= n:
            min_students += (n - count)
            n = count
        else:
            min_students += n
            break

    print(min_students)

main()
