
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    student_marks = {}
    for _ in range(n):
        name, *line = sys.stdin.readline().strip().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = sys.stdin.readline().strip()

    print("{0:.2f}".format(sum(student_marks[query_name])/3))
