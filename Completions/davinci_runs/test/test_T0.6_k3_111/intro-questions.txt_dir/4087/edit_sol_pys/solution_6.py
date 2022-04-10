
def solve(b):
    if b % 4 == 0:
        return b
    else:
        return b + (4 - b % 4)

def main():
    a = int(input())
    print solve(a)

if __name__ == "__main__":
    main()
