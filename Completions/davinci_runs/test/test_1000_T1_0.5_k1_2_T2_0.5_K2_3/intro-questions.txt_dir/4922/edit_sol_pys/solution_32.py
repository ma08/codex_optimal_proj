

def main():
    n, m = map(int, input().split())
    clauses = []
    for i in range(m):
        clauses.append(list(map(int, input().split())))
    if n < 8 or m < 8:
        print("unsatisfactory")
    else:
        print("satisfactory")

if __name__ == "__main__":
    main()
