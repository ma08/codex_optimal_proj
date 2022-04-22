
def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese = input().split()[1]
        if cheese not in cheeses:
            cheeses[cheese] = 0
        cheeses[cheese] += 1
    print(cheeses["soft"] if cheeses["soft"] < cheeses["hard"]
          else cheeses["hard"])

if __name__ == "__main__":
    main()
