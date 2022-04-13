
def get_input():
    x = int(input())
    return x

def process_data(x):
    if x == 0:
        return 1
    else:
        return 2

def print_data(result):
    print(result)

X, line = get_input()
num_people = process_data(X, line)
print_data(num_people)
