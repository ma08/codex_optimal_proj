
def f(x):
    x = x + 1
    while x % 10 == 0:
        x = x // 10
    return x

def main():
    x = int(input())
    memory = set()
    while x not in memory:
        memory.add(x)
        x = f(x)
    print(len(memory))

if __name__ == "__main__":
    main()
