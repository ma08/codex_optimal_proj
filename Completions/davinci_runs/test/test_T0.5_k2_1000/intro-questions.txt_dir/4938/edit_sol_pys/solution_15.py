

def get_input():
    X = int(raw_input())
    line = input()
    return X, line

def process_input(X, line):
    if X == 0:
        return len(line)
    else:
        return max(X+1, len(line) - X)

def print_output(num_characters):
    print(num_characters)

X, line = get_input()
num_characters = process_input(X, line)
print_output(num_characters)
