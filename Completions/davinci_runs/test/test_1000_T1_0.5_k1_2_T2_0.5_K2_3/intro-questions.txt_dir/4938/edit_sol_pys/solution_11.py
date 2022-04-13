

def get_input():
    N = int(input())
    line = input()
    return N, line

def process_input(N, line):
    if N == 0:
        return len(line)
    else:
        return max(N+1, len(line)-N)

def print_output(num_people):
    print(num_people)

N, line = get_input()
num_people = process_input(N, line)
print_output(num_people)
