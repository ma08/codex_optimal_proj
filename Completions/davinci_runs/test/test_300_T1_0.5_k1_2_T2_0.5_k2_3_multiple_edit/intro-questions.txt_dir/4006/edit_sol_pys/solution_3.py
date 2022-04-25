
def f(n):
    n = n + 1
    while n % 10 == 0:
        n = n // 10
    return n

def main():
    n = int(input())
    memory = set()
    while n not in memory:
        memory.add(n)
        n = f(n)
    print(len(memory)) 

if __name__ == "__main__":
    main()
