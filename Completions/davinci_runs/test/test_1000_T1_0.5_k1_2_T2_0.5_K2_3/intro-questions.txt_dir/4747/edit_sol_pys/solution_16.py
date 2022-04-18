

def run(input):
    n, k = [int(x) for x in input.readline().strip().split()]
    if k == 1:
        return n
    if k == 2:
        return (n + 1) / 2.0
    return (n + 1) / 2.0 + (n - 1) * ((k - 1) / (2.0 * k)) * (n + 1) / 2.0 + (n - 1) * ((k - 1) / (2.0 * k)) * ((n - 1) / 2.0) 
