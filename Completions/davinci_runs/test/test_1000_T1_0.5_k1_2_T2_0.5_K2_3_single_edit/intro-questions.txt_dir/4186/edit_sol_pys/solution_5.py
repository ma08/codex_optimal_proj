

from sys import stdin

def main():
    n = int(stdin.readline())#n is number of students
    skill_list = [int(x) for x in stdin.readline().split()]#skill_list is list of skills of students
    min_skill = min(skill_list)#min skill is the minimum skill

    # create a list of tuples of each skill and the number of students
    # with that skill
    skill_counts = []
    for i in range(min_skill, max(skill_list) + 1):#for i in range of min skill to max skill
        skill_counts.append((i, skill_list.count(i)))

    # sort the skill counts by the number of students with that skill
    skill_counts.sort(key=lambda x: x[1])#sort skill counts by skill count

    # find the minimum number of students needed to form a team
    # of each skill level
    min_students = 0
    for i, count in skill_counts:#for i in skill count and count in skill counts
        if count <= n:#if count is less than or equal to number of students
            min_students += (n - count)
            n = count
        else:
            min_students += n
            break

    print(min_students)#print min students

main()
