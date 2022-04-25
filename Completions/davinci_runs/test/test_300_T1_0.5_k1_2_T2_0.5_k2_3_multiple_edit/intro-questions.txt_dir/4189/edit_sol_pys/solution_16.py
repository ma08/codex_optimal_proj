

def main():
    n = int(input())
    cheese = {}
    for i in range(n):
        cheeses = input().split()
        if cheeses[1] not in cheese:
            cheese[cheeses[1]] = 0
        cheese[cheeses[1]] += 1
    print(cheese["soft"] if cheese["soft"] <= cheese["hard"] else cheese["hard"])

if __name__ == "__main__":
    main()
