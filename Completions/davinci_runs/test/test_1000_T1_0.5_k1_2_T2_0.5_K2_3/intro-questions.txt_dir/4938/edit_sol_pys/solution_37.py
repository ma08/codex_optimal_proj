

def get_input():
    X = int(input())
    line = input()
    return X, line.split()

def process_data(X, data):
    counter = 0
    for i in range(len(data)):
        if data[i] == '0':
            counter += 1
    return counter

def print_data(num_zeros):
    print(num_zeros)

X, data = get_input()
num_zeros = process_data(X, data)
print_data(num_zeros)
