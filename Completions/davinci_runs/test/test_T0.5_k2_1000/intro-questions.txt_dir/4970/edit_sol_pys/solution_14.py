#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.stdin.readline().strip())
    courses = {}
    for i in range(n):
        course_list = tuple(sorted([int(x) for x in sys.stdin.readline().strip().split()]))
        if course_list in courses.keys():
            courses[course_list] = courses[course_list] + 1
        else:
            courses[course_list] = 1
    max_count = max(courses.values())
    print(sum([courses[x] for x in courses if courses[x] == max_count]))

if __name__ == '__main__':
    main()
