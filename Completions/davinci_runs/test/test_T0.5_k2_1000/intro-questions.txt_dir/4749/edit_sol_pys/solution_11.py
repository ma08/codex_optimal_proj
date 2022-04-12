

def is_correct(grid):
    pass

if __name__ == '__main__':
    n = int(input())
    grid = [input() for _ in range(n)]
    if is_correct(grid):
        print(1)
    else:
        print(0)
