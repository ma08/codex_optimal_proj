
import sys

def read_input():
    """
    Reads the input and returns a list of tuples containing the minute and the answer.
    """
    contest_log = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '-1':
            break
        minute, problem, answer = line.split()
        contest_log.append((int(minute), problem, answer))
    return contest_log

def solve_contest(contest_log):
    """
    Solves the contest and returns the number of problems solved and the total time measure.
    """
    problems_solved = 0 
    time_measure = 0
    problems_wrong = {} #dictionary to store wrong answers
    for minute, problem, answer in contest_log:
        if answer == 'right':
            problems_solved += 1 
            time_measure += minute #add the minute to the time measure if correct
            if problem in problems_wrong:
                time_measure += problems_wrong[problem] * 20 #add the 20 minutes for each wrong answer
                del problems_wrong[problem]
        else:
            if problem not in problems_wrong:
                problems_wrong[problem] = 0
            problems_wrong[problem] += 1 #add one to the wrong answer
    return problems_solved, time_measure

def print_solution(solution):
    """
    Prints the solution in the specified format.
    """
    print(solution[0], solution[1]) #print the number of solved problems and the time measure

def main():
    contest_log = read_input()
    solution = solve_contest(contest_log)
    print_solution(solution)

if __name__ == '__main__':
    main()
