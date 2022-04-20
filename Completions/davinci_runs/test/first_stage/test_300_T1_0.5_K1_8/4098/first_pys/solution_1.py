

import sys

class Team(object):
    def __init__(self, student):
        self.students = [student]
        self.min = student
        self.max = student

    def add(self, student):
        self.students.append(student)
        self.min = min(self.min, student)
        self.max = max(self.max, student)
        return self.max - self.min <= 5

def solve(students, k):
    students.sort()
    teams = [Team(students[0])]
    for student in students[1:]:
        for team in teams:
            if team.add(student):
                break
        else:
            if len(teams) < k:
                teams.append(Team(student))
            else:
                return len(students) - 1
    return sum(len(team.students) for team in teams)

def main():
    n, k = map(int, sys.stdin.readline().split())
    students = map(int, sys.stdin.readline().split())
    print solve(students, k)

if __name__ == '__main__':
    main()