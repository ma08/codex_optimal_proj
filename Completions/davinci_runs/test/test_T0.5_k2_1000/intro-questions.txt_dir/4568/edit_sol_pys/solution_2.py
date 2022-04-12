

def solve(string):
    return str(len(set(string[:len(string)//2]) & set(string[len(string)//2:])))

print(solve(input()))
