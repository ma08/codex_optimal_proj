

def main():
    m, n = map(int, input().split()) # number of clauses and variables
    clauses = []
    for i in range(m):
        clauses.append(list(map(int, input().split())))
    if m < 9: # number of clauses
        print("unsatisfactory")
    else:
        print("satisfactory")

if __name__ == "__main__":
    main()
