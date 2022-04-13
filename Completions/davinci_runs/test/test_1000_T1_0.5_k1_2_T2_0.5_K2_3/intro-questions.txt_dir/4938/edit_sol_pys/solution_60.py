

def get_input():
    x = int(input())
    line = input().strip()
    return x, line

def process_input(x, line):
    if x == 0:
        return len(line)
    else:
        return max(x+1, len(line)-x)

def print_output(max_length):
    print(max_length)

x, line = get_input()
max_length = process_input(x, line)
print_output(max_length)
