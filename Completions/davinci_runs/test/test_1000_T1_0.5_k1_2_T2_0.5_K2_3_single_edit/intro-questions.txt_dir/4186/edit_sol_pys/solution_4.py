

from sys import stdin

def main():
    n = int(stdin.readline())
    skill_list = [int(x) for x in stdin.readline().split()] #List comprehension
    min_skill = min(skill_list)

    # create a list of tuples of each skill and the number of students
    # with that skill
    skill_counts = []
    for i in range(min_skill, max(skill_list) + 1): #range(start, stop, step)
        skill_counts.append((i, skill_list.count(i)))

    # sort the skill counts by the number of students with that skill
    skill_counts.sort(key=lambda x: x[1]) #x[1] is the second element of the tuple

    # find the minimum number of students needed to form a team
    # of each skill level
    min_students = 0
    for i, count in skill_counts:
        if count <= n: #count is the number of students with that skill
            min_students += (n - count) #n is the number of students who can be added to the team
            n = count #n is the number of students who can be added to the team
        else:
            min_students += n #n is the number of students who can be added to the team
            break

    print(min_students)

main()
