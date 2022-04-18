

def main():
    q = int(input())
    for _ in range(q):
        l1, r1, l2, r2 = map(int, input().split())  # a, b, c, d
        if l1 == r1:  # a == b
            print(l1, l2)  # print a c
        else:
            print(l1, l2+1)  # print a c+1

if __name__ == "__main__":
    main()
