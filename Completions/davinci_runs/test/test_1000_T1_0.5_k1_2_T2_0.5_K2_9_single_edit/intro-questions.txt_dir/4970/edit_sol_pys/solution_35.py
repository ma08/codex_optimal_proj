
import sys

def get_frosh_courses(n):
    return [sys.stdin.readline().strip().split() for i in range(n)]

def get_popularities(frosh_courses):
    return {tuple(sorted(frosh_course)): frosh_courses.count(frosh_course) for frosh_course in frosh_courses}

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
