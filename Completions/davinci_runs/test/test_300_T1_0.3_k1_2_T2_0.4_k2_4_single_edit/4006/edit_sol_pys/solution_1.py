

def f(x):
    return x + 1 if x % 10 else x // 10

def main():
    n = int(input())
    visited = {n}
    while True:
        if n in visited:
            break
        visited.add(n)
        n = f(n)
    print(len(visited))

if __name__ == "__main__":
    main()
