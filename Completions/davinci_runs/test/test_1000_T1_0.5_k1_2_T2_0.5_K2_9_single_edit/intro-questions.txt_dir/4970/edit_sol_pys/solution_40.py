

import sys

def get_frosh_courses(n):
    frosh_courses = []
    for i in range(n):
        frosh_courses.append(sys.stdin.readline().strip().split())
    return frosh_courses

def get_popularities(frosh_courses):
    popularities = {}
    for frosh_course in frosh_courses:
        frosh_course_tuple = tuple(sorted(frosh_course))
        if frosh_course_tuple in popularities:
            popularities[frosh_course_tuple] += 1
        else:
            popularities[frosh_course_tuple] = 1
    return popularities

def get_most_popularities(popularities):
    max_popularity = max(popularities.values())
    return [frosh_course_tuple for frosh_course_tuple, popularity in popularities.items() if popularity == max_popularity]

def main():
    n = int(sys.stdin.readline().strip())
    frosh_courses = get_frosh_courses(n)
    popularities = get_popularities(frosh_courses)
    most_popularities = get_most_popularities(popularities)
    print(len(most_popularities))

if __name__ == '__main__':
    main()
