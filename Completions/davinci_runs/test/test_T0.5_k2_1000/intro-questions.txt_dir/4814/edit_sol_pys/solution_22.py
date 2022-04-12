

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    if names == sorted(names):
        print("INCREASING ORDER")
    elif names == sorted(names, reverse=True):
        print("DECREASING ORDER")
    else: print("NEITHER")

if __name__ == "__main__":
    main()
