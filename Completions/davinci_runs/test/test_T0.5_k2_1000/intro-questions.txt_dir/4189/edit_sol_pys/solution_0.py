
def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        if cheese[1] == "soft":
            if "soft" not in cheeses:
                cheeses["soft"] = 0
            cheeses["soft"] += 1
        elif cheese[1] == "hard":
            if "hard" not in cheeses:
                cheeses["hard"] = 0
            cheeses["hard"] += 1
    print(cheeses["soft"] if cheeses["soft"] < cheeses["hard"] else cheeses["hard"])

if __name__ == "__main__":
    main()
