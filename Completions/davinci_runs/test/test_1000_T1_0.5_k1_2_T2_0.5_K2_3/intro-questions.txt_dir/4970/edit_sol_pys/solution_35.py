
import sys

def main():
    num_students = int(sys.stdin.readline().strip())
    courses = dict()
    for i in range(num_students):
        course_list = tuple(sorted(sys.stdin.readline().strip().split()))
        courses[course_list] = courses.get(course_list, 0) + 1
    max_count = max(courses.values())  # find the most popular course
    print(sum([courses[x] for x in courses if courses[x] == max_count]))  # count the most popular courses

if __name__ == '__main__':
    main()
