

def main():
    n = input()
    for i in range(len(n)):
        if n[i] != n[len(n)-1-i]:
            print("No")
            break
    else:
        print("Yes")

if __name__ == "__main__":
    main()
