

def main():
    m = input()
    r = int((len(m) ** .5) + 0.5)
    c = int((len(m) / r) + 0.5)
    for i in range(c):
        print(m[i::c], end="")

if __name__ == "__main__":
    main()
