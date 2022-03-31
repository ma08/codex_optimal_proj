

def solve(a):
    if a % 4 == 0:
        return a
    else:
        return a + (4 - a % 4)

def main():
    a = int(raw_input())
    print solve(a)

if __name__ == "__main__":
    main()