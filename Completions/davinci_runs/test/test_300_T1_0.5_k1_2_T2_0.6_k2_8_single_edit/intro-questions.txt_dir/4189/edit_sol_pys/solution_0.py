

def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        if cheese[1] not in cheeses:
            cheeses[cheese[1]] = 0
        cheeses[cheese[1]] += 1
    if "soft" in cheeses and "hard" in cheeses:
        print(cheeses["soft"] if cheeses["soft"] < cheeses["hard"] else cheeses["hard"])
    if "soft" in cheeses:
        print(cheeses["soft"])
    if "hard" in cheeses:
        print(cheeses["hard"])

if __name__ == "__main__":
    main()
