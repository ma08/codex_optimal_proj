

def get_input():
    X = int(input())
    line = input()
    return X, line

def process_input(X, line):
    if X == 0:
        return len(line)
    else:
        return max(len(line[:X]), len(line[X+1:]))

def print_output(max_length):
    print(max_length)

X, line = get_input()
max_length = process_input(X, line)
print_output(max_length)
