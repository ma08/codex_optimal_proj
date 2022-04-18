

def get_input():
    Y, line = map(int, input().split())
    line = input().split()
    return Y, line

def process_input(Y, line):
    if Y == 0:
        return len(set(line))
    else:
        return max(Y + 1, len(set(line)) - Y)

def print_output(num_people):
    print(num_people, end=" ")

Y, line = get_input()
num_people = process_input(Y, line)
print_output(num_people)
