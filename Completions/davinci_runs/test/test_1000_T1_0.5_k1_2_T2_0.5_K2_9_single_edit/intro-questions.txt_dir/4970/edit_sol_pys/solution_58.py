

import sys

def main():
    n = int(input())
    courses = {}
    for i in range(n):
        course_list = [int(x) for x in input().split()]
        course_list.sort()
        course_list = tuple(course_list)
        if course_list in courses:
            courses[course_list] += 1
        else:
            courses[course_list] = 1
    max_count = max(courses.values())
    print(len([courses[x] for x in courses if courses[x] == max_count]))

if __name__ == '__main__':
    main()
