

# This is a comment

import sys

def get_freshman_courses(n):
    freshman_courses = []
    for i in range(n):
        freshman_courses.append(sys.stdin.readline().strip().split())
    return freshman_courses

def get_popularities(freshman_courses):
    popularities = {}
    for freshman_course in freshman_courses:
        freshman_course_tuple = tuple(sorted(freshman_course))
        if freshman_course_tuple in popularities:
            popularities[freshman_course_tuple] += 1
        else:
            popularities[freshman_course_tuple] = 1
    return popularities

def get_most_popularities(popularities):
    most_popularities = []
    max_popularity = max(popularities.values())
    for freshman_course_tuple, popularity in popularities.items():
        if popularity == max_popularity:
            most_popularities.append(freshman_course_tuple)
    return most_popularities

def main():
    n = int(sys.stdin.readline().strip())
    freshman_courses = get_freshman_courses(n)
    popularities = get_popularities(freshman_courses)
    most_popularities = get_most_popularities(popularities)
    print(len(most_popularities))

if __name__ == '__main__':
    main()
