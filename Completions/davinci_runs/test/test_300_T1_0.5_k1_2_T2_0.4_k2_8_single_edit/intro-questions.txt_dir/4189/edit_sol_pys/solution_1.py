

def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()
        if cheese[1] in cheeses:
            cheeses[cheese[1]] += 1
        else:
            cheeses[cheese[1]] = 1
    print(min(cheeses["soft"], cheeses["hard"]))

if __name__ == "__main__":
    main()
