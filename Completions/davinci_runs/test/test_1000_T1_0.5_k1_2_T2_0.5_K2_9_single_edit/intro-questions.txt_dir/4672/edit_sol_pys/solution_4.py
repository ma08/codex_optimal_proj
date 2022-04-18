
# Enter your code here. Read input from STDIN. Print output to STDOUT

def average(array):
    return sum(array) / len(array)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(average(student_marks[query_name]))
