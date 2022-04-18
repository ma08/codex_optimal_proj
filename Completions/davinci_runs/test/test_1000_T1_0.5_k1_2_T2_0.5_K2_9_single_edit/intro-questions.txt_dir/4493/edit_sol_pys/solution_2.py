

def main():
    lst = []
    for i in range(3):
        lst.append(list(map(int, input().split())))

    for a1 in range(101):
        for a2 in range(101):
            for a3 in range(101):
                for b1 in range(101):
                    for b2 in range(101):
                        for b3 in range(101):
                            if lst[0][0] == a1 + b1 and lst[0][1] == a1 + b2 and lst[0][2] == a1 + b3 and lst[1][0] == a2 + b1 and lst[1][1] == a2 + b2 and lst[1][2] == a2 + b3 and lst[2][0] == a3 + b1 and lst[2][1] == a3 + b2 and lst[2][2] == a3 + b3:
                                print("Yes")
                                exit()
    print("No")

if __name__ == "__main__":
    main()
