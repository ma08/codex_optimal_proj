
import sys

def get_frosh_courses(n, courses):
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

def get_most_popular_courses(popularities):
    most_popular_courses = []
    max_popularity = max(popularities.values())
    for course_tuple, popularity in popularities.items():
        if popularity == max_popularity:
            most_popular_courses.append(course_tuple)
    return most_popular_courses

def main():
    courses = []
    n = int(sys.stdin.readline().strip())
    courses = get_frosh_courses(n, courses)
    popularities = get_popularities(courses)
    most_popular_courses = get_most_popular_courses(popularities)
    print(len(most_popular_courses))

if __name__ == '__main__':
    main()
