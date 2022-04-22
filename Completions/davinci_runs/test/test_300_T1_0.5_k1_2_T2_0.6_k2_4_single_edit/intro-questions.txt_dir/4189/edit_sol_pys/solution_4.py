

def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        if cheese[1] not in cheeses:
            cheeses[cheese[1]] = 0
        cheeses[cheese[1]] += 1
    print(cheeses["soft"] if cheeses.get("soft", 0) < cheeses.get("hard", 0) else cheeses["hard"])

if __name__ == "__main__":
    main()
