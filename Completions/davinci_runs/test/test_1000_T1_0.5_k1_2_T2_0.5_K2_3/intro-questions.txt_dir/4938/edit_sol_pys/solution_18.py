

def get_input():
    Y = int(input())
    line = input()
    return Y, line

def process_input(Y, line):
    if Y == 0:
        return len(line)
    return max(Y+1, len(line)-Y)

def print_output(num_people):
    print(num_people)

Y, line = get_input()
num_people = process_input(Y, line)
print_output(num_people)
