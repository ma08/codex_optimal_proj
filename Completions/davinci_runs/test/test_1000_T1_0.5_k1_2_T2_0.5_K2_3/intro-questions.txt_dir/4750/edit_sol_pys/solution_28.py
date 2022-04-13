
def main():
    q = int(input()) # number of test cases
    for _ in range(q): # iterate through each test case
        l1, r1, l2, r2 = map(int, input().split())
        if l1 == r1:
            print(l1, l2) # print the answer
        else:
            print(l1, l2+1) # print the answer

if __name__ == "__main__":
    main()
