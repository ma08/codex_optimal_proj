

def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input()
        if cheese not in cheeses:
            cheeses[cheese] = 0
        cheeses[cheese] += 1
    print(cheeses["S"] if cheeses["S"] < cheeses["H"] else cheeses["H"])

if __name__ == "__main__":
    main()
