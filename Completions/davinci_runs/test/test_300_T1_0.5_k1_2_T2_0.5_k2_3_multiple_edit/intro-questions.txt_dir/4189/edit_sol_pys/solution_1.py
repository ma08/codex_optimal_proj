

def main():
    n = int(input())
    cheese = {"soft": 0, "hard": 0}
    for i in range(n):
        cheeses = input().split()
        cheese[cheeses[1]] += 1
    print(cheese["soft"] if cheese["soft"] < cheese["hard"] else cheese["hard"])

if __name__ == "__main__":
    main()
