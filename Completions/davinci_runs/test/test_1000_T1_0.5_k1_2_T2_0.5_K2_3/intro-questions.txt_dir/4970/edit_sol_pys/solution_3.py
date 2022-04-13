

import sys

def get_courses(n):
    courses = []
    for i in range(n):
        courses.append(sys.stdin.readline().strip().split())
    return courses

def get_popularities(courses):
    popularities = {}
    for course in courses:
        course_tuple = tuple(sorted(course))
        if course_tuple in popularities:
            popularities[course_tuple] += 1
        else:
            popularities[course_tuple] = 1
    return popularities

def get_most_popular(popularities):
    most_popular = []
    max_popularity = max(popularities.values())
    for course_tuple, popularity in popularities.items():
        if popularity == max_popularity:
            most_popular.append(course_tuple)
    return most_popular

def main():
    n = int(sys.stdin.readline().strip())
    courses = get_courses(n)
    popularities = get_popularities(courses)
    most_popular = get_most_popular(popularities)
    print(len(most_popular))

if __name__ == '__main__':
    main()
