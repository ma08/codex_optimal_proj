


class Problem:
    def __init__(self, name, contest, index):
        self.name = name
        self.contest = contest
        self.index = index

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Contest:
    def __init__(self, name, problems):
        self.name = name
        self.problems = problems

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Problemset:
    def __init__(self, problems):
        self.problems = problems
        self.contests = set()
        for problem in problems:
            self.contests.add(problem.contest)

    def __str__(self):
        return str(self.problems)

    def __repr__(self):
        return str(self.problems)


def get_max_contest(problemset):
    pass

# TODO: make solution


def get_problemset():
    problems = [
        Problem("A", "Educational Codeforces Round 1", 1),
        Problem("B", "Educational Codeforces Round 1", 2),
        Problem("C", "Educational Codeforces Round 1", 3),
        Problem("D", "Educational Codeforces Round 1", 4),
        Problem("E", "Educational Codeforces Round 1", 5),
        Problem("F", "Educational Codeforces Round 1", 6),
        Problem("G", "Educational Codeforces Round 1", 7),
        Problem("H", "Educational Codeforces Round 1", 8),
        Problem("A", "Educational Codeforces Round 2", 1),
        Problem("B", "Educational Codeforces Round 2", 2),
        Problem("C", "Educational Codeforces Round 2", 3),
        Problem("D", "Educational Codeforces Round 2", 4),
        Problem("E", "Educational Codeforces Round 2", 5),
        Problem("F", "Educational Codeforces Round 2", 6),
        Problem("G", "Educational Codeforces Round 2", 7),
        Problem("H", "Educational Codeforces Round 2", 8),
        Problem("A", "Educational Codeforces Round 3", 1),
        Problem("B", "Educational Codeforces Round 3", 2),
        Problem("C", "Educational Codeforces Round 3", 3),
        Problem("D", "Educational Codeforces Round 3", 4),
        Problem("E", "Educational Codeforces Round 3", 5),
        Problem("F", "Educational Codeforces Round 3", 6),
        Problem("G", "Educational Codeforces Round 3", 7),
        Problem("H", "Educational Codeforces Round 3", 8),
        Problem("A", "Educational Codeforces Round 4", 1),
        Problem("B", "Educational Codeforces Round 4", 2),
        Problem("C", "Educational Codeforces Round 4", 3),
        Problem("D", "Educational Codeforces Round 4", 4),
        Problem("E", "Educational Codeforces Round 4", 5),
        Problem("F", "Educational Codeforces Round 4", 6),
        Problem("G", "Educational Codeforces Round 4", 7),
        Problem("H", "Educational Codeforces Round 4", 8),
    ]
    return Problemset(problems)


if __name__ == "__main__":
    problemset = get_problemset()
    print(problemset)
