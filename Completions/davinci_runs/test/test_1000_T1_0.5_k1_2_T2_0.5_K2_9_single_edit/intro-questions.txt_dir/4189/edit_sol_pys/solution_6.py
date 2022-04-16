

def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        if cheese[2] not in cheeses:
            cheeses[cheese[2]] = 0
        cheeses[cheese[2]] += 1
    print(cheeses["soft"] if cheeses["soft"] < cheeses["hard"] else cheeses["hard"])

if __name__ == "__main__":
    main()
