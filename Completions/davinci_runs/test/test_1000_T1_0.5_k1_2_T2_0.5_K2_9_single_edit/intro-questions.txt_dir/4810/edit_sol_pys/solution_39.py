

def main():
    m = input()
    c = int(len(m) ** .5)
    r = int(len(m) / c)
    for i in range(c):
        print(m[i::c], end="")

if __name__ == "__main__":
    main()
