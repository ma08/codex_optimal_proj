
def main():
    n = int(input())
    cheeses = {}
    for i in range(n):
        cheese, hardness = input().split()
        if hardness not in cheeses:
            cheeses[hardness] = 0
        cheeses[hardness] += 1
    print(cheeses["soft"] if cheeses["soft"] < cheeses["hard"] else cheeses["hard"])

if __name__ == "__main__":
    main()
