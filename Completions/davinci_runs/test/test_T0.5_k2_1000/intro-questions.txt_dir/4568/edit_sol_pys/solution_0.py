

def solve(string):
    return len(set(string[:len(string)//2]) & set(string[len(string)//2:])) if len(string) % 2 == 0 else -1

print(solve(input()))
