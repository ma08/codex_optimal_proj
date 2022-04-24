

from sys import stdin
from typing import List, Tuple



def get_max_num_projects(rating: int, projects: List[Tuple[int, int]]):
    num_projects = 0
    for required_rating, rating_change in projects:
        if rating >= required_rating:
            rating += rating_change
            num_projects += 1

    return num_projects


def main():
    input_line = stdin.readline().split()
    num_projects, initial_rating = int(input_line[0]), int(input_line[1])
    projects: List[Tuple[int, int]] = []
    for _ in range(num_projects):
        project_rating, rating_change = stdin.readline().split()
        projects.append((int(project_rating), int(rating_change)))

    projects.sort(key=lambda x: x[1])
    projects.sort(key=lambda x: x[0])
    print(get_max_num_projects(initial_rating, projects))


if __name__ == '__main__':
    main()
