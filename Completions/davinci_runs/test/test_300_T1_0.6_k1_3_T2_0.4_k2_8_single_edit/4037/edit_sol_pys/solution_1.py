

from sys import stdin
from typing import List, Tuple, Dict


def get_max_num_projects(rating: int, projects: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    new_projects = []
    for i, (required_rating, rating_change) in enumerate(projects):
        if rating >= required_rating: new_projects.append((i, rating_change))

    return new_projects


def get_max_num_projects_helper(rating: int, projects: List[Tuple[int, int]]) -> int:
    if len(projects) == 0: return 0

    max_num_projects = 0
    for index, rating_change in projects:
        new_rating = rating + rating_change
        new_projects = projects[:index] + projects[index + 1:]
        max_num_projects = max(max_num_projects, 1 + get_max_num_projects_helper(new_rating, new_projects))

    return max_num_projects


def main() -> None:
    input_line = stdin.readline().split()
    num_projects, initial_rating = int(input_line[0]), int(input_line[1])
    projects: List[Tuple[int, int]] = []
    for _ in range(num_projects):
        project_rating, rating_change = stdin.readline().split()
        projects.append((int(project_rating), int(rating_change)))

        projects.append((int(project_rating), int(rating_change)))

    new_projects = get_max_num_projects(initial_rating, projects)
    new_projects.sort(key=lambda x: x[1])
    new_projects.sort(key=lambda x: x[0])
    print(get_max_num_projects_helper(initial_rating, new_projects))


if __name__ == '__main__':
    main()
