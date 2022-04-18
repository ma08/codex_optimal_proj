

def main():
    num = int(input())
    names = []

    for i in range(num):
        names.append(input())

    if names == sorted(names):
        print("INCREASING") 
    elif names == sorted(names, reverse=True):
        print("DECREASING")
    else:
        print("NEITHER")

if __name__ == "__main__":
    main()
