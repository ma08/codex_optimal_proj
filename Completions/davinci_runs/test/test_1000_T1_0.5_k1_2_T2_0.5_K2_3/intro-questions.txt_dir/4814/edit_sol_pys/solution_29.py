

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    if all(names[i] <= names[i+1] for i in range(n-1)):
        print("INCREASING ORDER")
        return
    if all(names[i] >= names[i+1] for i in range(n-1)):
        print("DECREASING ORDER")
        return
    print("NEITHER")

if __name__ == "__main__":
    main()
