import sys

def find_popular_combinations(frosh):
    combinations = {}
    for combination in frosh:
        if combination in combinations:
            combinations[combination] += 1
        else:
            combinations[combination] = 1

    most_popular = max(combinations.values())
    return most_popular

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    frosh = set()
    for i in range(n):
        frosh.add(tuple(sorted([int(x) for x in sys.stdin.readline().strip().split()])))
    print(find_popular_combinations(frosh))
