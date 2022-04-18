

def main():
    m, n = map(int, input().split()) # m is the number of clauses, n is the number of variables
    clauses = []
    for i in range(m):
        clauses.append(list(map(int, input().split()))) # each line is a clause
    if m < 8:
        print("unsatisfactory")
    else:
        print("satisfactory")

if __name__ == "__main__":
    main()
