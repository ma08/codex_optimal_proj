

def get_input(file):
    X = int(file.readline())
    line = file.readline()
    return int(X), line

def process_input(X, line, file):
    if X == 0:
        return len(line)
    else:
        return max(X+1, len(line)-X)

def print_output(max_length, file):
    file.write(str(max_length))

X, line = get_input()
max_length = process_input(X, line)
print_output(max_length)
