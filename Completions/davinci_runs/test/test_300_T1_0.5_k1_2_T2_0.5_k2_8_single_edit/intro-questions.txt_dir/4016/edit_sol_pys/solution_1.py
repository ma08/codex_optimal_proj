

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))  # a = [1, 2, 3]
    bc = []
    for _ in range(m):
        bc.append(list(map(int, input().split())))
    bc = sorted(bc, key=lambda x: x[1], reverse=True)
    bc = sorted(bc, key=lambda x: x[0])
    print(bc)
    for i in range(m):
        for j in range(bc[i][0]):
            a[j] = bc[i][1]
    print(sum(a))

if __name__ == "__main__":
    main()
