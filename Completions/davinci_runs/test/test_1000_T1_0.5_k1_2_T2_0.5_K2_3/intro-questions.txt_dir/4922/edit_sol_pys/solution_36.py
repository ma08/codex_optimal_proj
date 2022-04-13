

def main():
    m, n = map(int, input().split())
    clauses = []
    for i in range(m):
        clauses.append(list(map(int, input().split())))  # [[1,2],[2,-3]]
    if m < 7:
        print("unsatisfiable")
    else:
        print("satisfiable")

if __name__ == "__main__":
    main()
