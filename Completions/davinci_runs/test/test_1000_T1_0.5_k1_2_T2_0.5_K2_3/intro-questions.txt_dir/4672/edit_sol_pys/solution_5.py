# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    n = int(raw_input())
    students = []
    scores = []
    for _ in range(n):
        name = raw_input()
        score = float(raw_input())
        students.append([name, score])
        scores.append(score)
    second_lowest_score = sorted(list(set(scores)))[1]
    students = sorted(students, key=lambda x: x[1])
    for i in students:
        if i[1] == second_lowest_score:
            print i[0]
