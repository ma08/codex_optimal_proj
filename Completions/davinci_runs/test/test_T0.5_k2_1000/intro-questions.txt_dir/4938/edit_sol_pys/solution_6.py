

def get_input():
    x = int(input())
    line = input()
    return x, line

def process_input(x, line):
    if x == 0:
        return len(line)
    else:
        return max(x+1, len(line)-x)

def print_output(num_characters):
    print(num_characters)

x, line = get_input()
num_characters = process_input(x, line)
print_output(num_characters)
