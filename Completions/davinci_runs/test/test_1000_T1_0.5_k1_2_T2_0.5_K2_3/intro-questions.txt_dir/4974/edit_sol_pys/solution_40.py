
# Solution by Andrei Negura (UBB)

def main():
    r, n = [int(i) for i in raw_input().split()]
    booked = set()
    for i in range(n):
        booked.add(int(raw_input()))
    for i in range(1, r+1):
        if i not in booked:
            print(i)
            return
    print("too late")

if __name__ == "__main__":
    main()
