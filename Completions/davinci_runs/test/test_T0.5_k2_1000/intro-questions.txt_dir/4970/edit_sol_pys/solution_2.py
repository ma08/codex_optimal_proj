import sys

def find_popular_combinations(frosh):
    combinations = {}
    for combination in frosh:
        combination.sort()
        combination = tuple(combination)
        if combination in combinations:
            combinations[combination] += 1
        else:
            combinations[combination] = 1
    most_popular = max(combinations.values())
    return [combination for combination in combinations if combinations[combination] == most_popular]

if __name__ == '__main__':
    n = int(input().strip())
    frosh = []
    for i in range(n):
        frosh.append([int(x) for x in input().strip().split()])
    print(len(find_popular_combinations(frosh)))
