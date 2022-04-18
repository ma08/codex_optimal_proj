

def main():
    q = int(input())
    for _ in range(q):
        l1, r1, l2, r2 = map(int, input().split())  # taking input
        if l1 == r1:  # if l1 and r1 is same then print l1 and l2
            print(l1, l2) 
        else:
            print(l1, l2+1)


if __name__ == "__main__":
    main()
