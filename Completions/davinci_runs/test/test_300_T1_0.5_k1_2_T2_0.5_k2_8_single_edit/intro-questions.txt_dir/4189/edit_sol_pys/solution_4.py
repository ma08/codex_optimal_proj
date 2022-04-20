

def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        if cheese[1] == "soft":
            if cheese[4] not in cheeses:
                cheeses[cheese[4]] = 0
            cheeses[cheese[4]] += 1
        else:
            if cheese[3] not in cheeses:
                cheeses[cheese[3]] = 0
            cheeses[cheese[3]] += 1
    print(cheeses["soft"] if cheeses["soft"] < cheeses["hard"] else cheeses["hard"])

if __name__ == "__main__":
    main()
