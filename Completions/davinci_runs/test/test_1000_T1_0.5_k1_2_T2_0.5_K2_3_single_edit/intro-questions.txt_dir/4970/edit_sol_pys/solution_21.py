

import sys

def main():
    num_cases = int(sys.stdin.readline().strip())
    for i in range(num_cases):
        num_frosh = int(sys.stdin.readline().strip())
        course_counts = {}
        for j in range(num_frosh):
            course_combination = tuple(sorted(map(int, sys.stdin.readline().strip().split())))
            course_counts[course_combination] = course_counts.get(course_combination, 0) + 1
        print max(course_counts.values())

if __name__ == '__main__':
    main()
