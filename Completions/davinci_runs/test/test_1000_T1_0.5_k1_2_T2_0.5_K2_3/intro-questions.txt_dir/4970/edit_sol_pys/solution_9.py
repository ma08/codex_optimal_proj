#!/usr/bin/env python3

import sys

def main():
    num_students = int(input())
    courses = dict()
    for i in range(num_students):
        course_list = tuple(sorted([int(x) for x in input().strip().split()]))
        courses[course_list] = courses.get(course_list, 0) + 1
    max_count = max(courses.values())  # find the most popular course
    print(sum([courses[x] for x in courses if courses[x] == max_count]))  # count the most popular courses

if __name__ == '__main__':
    main()
