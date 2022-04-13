
def get_input():
    X = int(input())
    line = input()
    return X, line

def process_data(X, line):
    if X == 0:
        return len(line)
    else:
        return max(X+1, len(line)-X)

def print_data(num_people):
    print(num_people)

X, line = get_input()
num_people = process_data(X, line)
print_data(num_people)
