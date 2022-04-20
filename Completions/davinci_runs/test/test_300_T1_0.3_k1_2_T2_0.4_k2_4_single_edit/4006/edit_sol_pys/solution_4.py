

def f(x):
    while x % 10 == 0: x //= 10
    return x + 1 

def main():
    n = int(input())
    visited = set()
    while n not in visited: visited.add(n); n = f(n)
    print(len(visited))

if __name__ == "__main__":
    main()
