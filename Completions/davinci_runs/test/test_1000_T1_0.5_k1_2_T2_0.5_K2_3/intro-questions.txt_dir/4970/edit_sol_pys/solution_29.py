

import sys

def get_fresh_courses(n):
    fresh_courses = []
    for i in range(n):
        fresh_courses.append(sys.stdin.readline().strip().split(' '))
    return fresh_courses

def get_popularities(fresh_courses):
    popularities = {}
    for fresh_course in fresh_courses:
        fresh_course_tuple = tuple(sorted(fresh_course))
        if fresh_course_tuple in popularities:
            popularities[fresh_course_tuple] += 1
        else:
            popularities[fresh_course_tuple] = 1
    return popularities

def get_most_popularities(popularities):
    most_popularities = []
    max_popularity = max(popularities.values())
    for fresh_course_tuple, popularity in popularities.items():
        if popularity == max_popularity:
            most_popularities.append(fresh_course_tuple)
    return most_popularities

def main():
    n = int(sys.stdin.readline().strip())
    fresh_courses = get_fresh_courses(n)
    popularities = get_popularities(fresh_courses)
    most_popularities = get_most_popularities(popularities)
    print(len(most_popularities))

if __name__ == '__main__':
    main()
