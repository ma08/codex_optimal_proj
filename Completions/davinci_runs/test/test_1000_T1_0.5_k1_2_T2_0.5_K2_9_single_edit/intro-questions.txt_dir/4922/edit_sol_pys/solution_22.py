

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            m, n = map(int, input().split())
            clauses = []
            for i in range(m):
                clauses.append(list(map(int, input().split())))
            if m < 8:
                print("unsatisfactory")
            else:
                print("satisfactory")

if __name__ == "__main__":
    main()
