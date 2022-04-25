

def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        if cheese[1] not in cheeses:
            cheeses[cheese[1]] = 0
        cheeses[cheese[1]] += 1
    print(cheeses["S"] if cheeses["S"] <= cheeses["H"] else cheeses["H"])

if __name__ == "__main__":
    main()
