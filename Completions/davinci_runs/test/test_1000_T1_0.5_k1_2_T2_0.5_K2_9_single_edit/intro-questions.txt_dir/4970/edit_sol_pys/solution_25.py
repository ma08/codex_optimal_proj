
import sys

def main():
    frosh = int(sys.stdin.readline().strip())
    course_counts = {}
    for i in range(frosh):
        course_combination = tuple(sorted(map(int, sys.stdin.readline().strip().split())))
        course_counts[course_combination] = course_counts.get(course_combination, 0) + 1
    print(max(course_counts.values()))

if __name__ == '__main__':
    main()
