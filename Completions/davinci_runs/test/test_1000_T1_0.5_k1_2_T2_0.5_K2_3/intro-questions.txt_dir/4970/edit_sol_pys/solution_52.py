
import sys

def find_popular_combinations(frosh):
    combinations = {}
    for i in range(len(frosh)):
        combination = frosh[i]
        combination.sort()
        combination = tuple(combination)
        if combination in combinations:
            combinations[combination] += 1
        else:
            combinations[combination] = 1
    most_popular = max(combinations.values())
    return [combination for combination in combinations if combinations[combination] == most_popular]

if __name__ == '__main__':
    num_frosh = int(sys.stdin.readline().strip())
    frosh = []
    for i in range(num_frosh):
        frosh.append([int(x) for x in sys.stdin.readline().strip().split()])
    print(len(find_popular_combinations(frosh)))
