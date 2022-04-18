

def main():
    s = input()
    n = len(s)
    a = s.count('a')
    print(min(n, 2 * a - 1))
