

def main():
    m = input().strip()
    r = int(len(m) ** .5) + 1
    for i in range(r):
        print(m[i::r], end="")

if __name__ == "__main__":
    main()
