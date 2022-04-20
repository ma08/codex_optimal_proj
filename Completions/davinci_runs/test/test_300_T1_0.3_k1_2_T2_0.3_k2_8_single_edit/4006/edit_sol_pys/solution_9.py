

def f(x):
    return x + 1 if x % 10 != 0 else x // 10 + 1

def main():
    n = int(input())
    visited = set()
    while n not in visited:
        visited.add(n)
        n = f(n)
    print(len(visited))

if __name__ == "__main__":
    main()
