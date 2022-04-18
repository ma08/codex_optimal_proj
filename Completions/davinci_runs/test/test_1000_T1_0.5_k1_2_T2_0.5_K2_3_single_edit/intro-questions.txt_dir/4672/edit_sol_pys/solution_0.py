


def get_average_score(student_marks, query_name):
    marks = student_marks.get(query_name)
    return sum(marks)/len(marks)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(get_average_score(student_marks, query_name)))
