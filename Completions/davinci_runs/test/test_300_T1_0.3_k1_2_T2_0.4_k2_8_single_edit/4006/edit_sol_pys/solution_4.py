

def f(x):
    return x + 2

def main():
    n = int(input())
    visited = set()
    while n not in visited:
        visited.add(n)
        n = f(n)
    print(len(visited))

if __name__ == "__main__":
    main()
