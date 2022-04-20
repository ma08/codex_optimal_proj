

def main():
    n = input()
    if len(n) == 1 or len(n) == 2:
        print("Yes")
        return
    if n[0] == n[-1]:
        print("Yes")
        return
    print("No")
    return

if __name__ == "__main__":
    main()
