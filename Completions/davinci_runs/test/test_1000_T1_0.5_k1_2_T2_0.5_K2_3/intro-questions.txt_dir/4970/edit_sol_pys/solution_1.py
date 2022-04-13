
import sys

def find_popular_combinations(n):
    combinations = {}
    for i in range(n):
        combination = frog[i]
        combination.sort()
        combination = tuple(combination)
        if combination in combinations:
            combinations[combination] += 1
        else:
            combinations[combination] = 1
    most_popular = max(combinations.values())
    return [combination for combination in combinations if combinations[combination] == most_popular]

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    frog = []
    for i in range(n):
        frog.append([int(x) for x in sys.stdin.readline().strip().split()])
    print(len(find_popular_combinations(n)))
