"""
@author: xueqiang.liu
"""
import sys

def main():
    while True:
        try:
            freshmen = int(sys.stdin.readline().strip())
            course_counts = {}
            for i in range(freshmen):
                course_combination = tuple(sorted(map(int, sys.stdin.readline().strip().split())))
                course_counts[course_combination] = course_counts.get(course_combination, 0) + 1
            print max(course_counts.values())
        except:
            break
if __name__ == '__main__':
    main()
