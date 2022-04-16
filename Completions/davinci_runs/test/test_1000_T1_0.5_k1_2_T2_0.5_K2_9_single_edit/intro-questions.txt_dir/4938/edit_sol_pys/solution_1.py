

def get_input():
    X = int(input())
    line = input()
    return X, line

def process_input(X, line):
    if X == 0:
        return len(line)
    else:
        return max(X+1, len(line))

def print_output(num_people):
    print(num_people)

X, line = get_input()
num_people = process_input(X, line)
print_output(num_people)
