
def minimum_cost_bottles(n, a, b, c):
    return min(n*a, n//2*b + n%2*a, n//3*c + n%3*a)

def main():
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    for query in queries:
        print(minimum_cost_bottles(query[0], query[1], query[2], query[3]))

if __name__ == "__main__":
    main()
