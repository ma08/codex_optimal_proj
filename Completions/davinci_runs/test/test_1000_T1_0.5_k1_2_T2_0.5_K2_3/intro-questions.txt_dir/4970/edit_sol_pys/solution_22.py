import sys

def find_popular_combinations(n, frosh):
    combinations = {} # dictionary of combinations and their occurences
    for i in range(n):
        combination = frosh[i] # get the courses for student i
        combination.sort() # sort courses
        combination = tuple(combination) # convert to tuple
        if combination in combinations:
            combinations[combination] += 1 # increment occurences
        else:
            combinations[combination] = 1 # add to dictionary
    most_popular = max(combinations.values()) # get the max occurences
    return [combination for combination in combinations if combinations[combination] == most_popular] # return all combinations with max occurences

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip()) # get number of students
    frosh = []
    for i in range(n):
        frosh.append([int(x) for x in sys.stdin.readline().strip().split()]) # get courses for each student
    print(len(find_popular_combinations(n, frosh))) # print number of popular combinations
