

def main():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    for i in range(n-1):
        if names[i+1] < names[i]:
            break
    else:
        print("INCREASING")
        return
    for i in range(n-1):
        if names[i+1] > names[i]:
            break
    else:
        print("DECREASING")
        return
    print("NEITHER")

if __name__ == "__main__":
    main()
