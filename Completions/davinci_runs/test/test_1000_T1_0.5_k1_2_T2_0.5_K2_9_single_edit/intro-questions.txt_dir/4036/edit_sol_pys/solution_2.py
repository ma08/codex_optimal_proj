
def main():
    n = int(input())
    d = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        d[name] = scores
    query_name = input()
    print("{:.2f}".format(sum(d[query_name])/3))

if __name__ == "__main__":
    main()
