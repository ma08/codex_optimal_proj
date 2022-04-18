
import sys

def main():
    n = int(sys.stdin.readline().strip())
    courses = []
    for i in range(n):
        courses.append(sys.stdin.readline().strip())
    courses.sort()
    max_count = 0
    count = 1
    for i in range(len(courses) - 1):
        if courses[i] == courses[i + 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 1
    if count > max_count:
        max_count = count
    print(max_count)

if __name__ == '__main__':
    main()
