

def main():
    n = int(input())
    cheeses = {"soft": 0, "hard": 0}
    for i in range(n):
        cheese = input().split()
        cheeses[cheese[1]] += 1
    print(min(cheeses["soft"], cheeses["hard"]))

if __name__ == "__main__":
    main()
