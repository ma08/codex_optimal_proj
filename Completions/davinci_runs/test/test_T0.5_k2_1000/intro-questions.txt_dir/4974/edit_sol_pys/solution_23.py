
# Solution 

def main():
    r, n = [int(i) for i in input().split()]
    booked = set()
    for i in range(n):
        booked.add(int(input()))
    for i in range(1, r+1):
        if i not in booked:
            print(i)
            return
    print("too late")

if __name__ == "__main__":
    main()
