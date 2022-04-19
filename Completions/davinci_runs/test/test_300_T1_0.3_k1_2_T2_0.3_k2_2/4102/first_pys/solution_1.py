

def main():
    n = input()
    if len(n) == 1:
        print("Yes")
        return
    if len(n) == 2:
        if n[0] == n[1]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(n) == 3:
        if n[0] == n[2]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(n) == 4:
        if n[0] == n[3] and n[1] == n[2]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(n) == 5:
        if n[0] == n[4] and n[1] == n[3]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(n) == 6:
        if n[0] == n[5] and n[1] == n[4] and n[2] == n[3]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(n) == 7:
        if n[0] == n[6] and n[1] == n[5] and n[2] == n[4]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(n) == 8:
        if n[0] == n[7] and n[1] == n[6] and n[2] == n[5] and n[3] == n[4]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(n) == 9:
        if n[0] == n[8] and n[1] == n[7] and n[2] == n[6] and n[3] == n[5]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(n) == 10:
        if n[0] == n[9] and n[1] == n[8] and n[2] == n[7] and n[3] == n[6] and n[4] == n[5]:
            print("Yes")
            return
        else:
            print("No")
            return

if __name__ == "__main__":
    main()