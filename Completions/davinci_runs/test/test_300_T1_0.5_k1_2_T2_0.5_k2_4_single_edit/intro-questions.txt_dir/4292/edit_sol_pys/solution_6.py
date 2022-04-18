

def read_file(filename):
    with open(filename) as f:
        return f.read()

def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

print(sum(prices[:k]))
