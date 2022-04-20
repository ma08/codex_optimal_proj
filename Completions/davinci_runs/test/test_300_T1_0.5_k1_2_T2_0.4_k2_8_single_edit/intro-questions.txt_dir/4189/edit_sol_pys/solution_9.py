

def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        if cheese[1] not in cheeses:
            cheeses[cheese[1]] = 0
    if "soft" not in cheeses:
        cheeses["soft"] = 0
    if "hard" not in cheeses:
        cheeses["hard"] = 0
        cheeses[cheese[1]] += 1
    print(cheeses["soft"] if cheeses["soft"] < cheeses["hard"] else cheeses["hard"])

if __name__ == "__main__":
    main()
