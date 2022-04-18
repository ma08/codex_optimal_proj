
def problem_solve(input_list):
    """input_list: list of integers"""
    n = len(input_list)
    x_list = input_list
    mean = sum(x_list) / n
    return sum([(x - mean)**2 for x in x_list])

if __name__ == '__main__':
    n = int(input())
    x_list = [int(x) for x in input().split()]
    print(problem_solve(x_list))
