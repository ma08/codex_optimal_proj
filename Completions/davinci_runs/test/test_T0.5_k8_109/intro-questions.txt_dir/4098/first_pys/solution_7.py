

def get_max_students(students, num_teams):
    students.sort()

    max_students = 0
    for team_size in range(1, len(students) + 1):
        if num_teams < len(students) / team_size:
            continue

        total_students = 0
        for i in range(0, len(students), team_size):
            team = students[i:i + team_size]
            if team[-1] - team[0] > 5:
                continue

            total_students += len(team)

        max_students = max(max_students, total_students)

    return max_students


def main():
    n, k = [int(x) for x in input().split()]
    students = [int(x) for x in input().split()]

    print(get_max_students(students, k))


if __name__ == "__main__":
    main()