

# SOLUTION

def main():
    q = int(input())
    for i in range(q):
        n = int(input())
        m = 1
        while m < n:
            m *= 3
        print(m)


if __name__ == "__main__":
    main()
