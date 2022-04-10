

import sys

def main():
    n, d, k = map(int, input().split())
    
    if d == 1:
        if n == 1 and k >= 1:
            print("YES")
        else:
            print("NO")
        sys.exit()
    
    if n == 2:
        if d == 2 and k >= 2:
            print("YES")
            print("1 2")
        else:
            print("NO")
        sys.exit()
    
    if d == 2:
        if k >= 2:
            print("YES")
            for i in range(n - 1):
                print(i + 1, i + 2)
        else:
            print("NO")
        sys.exit()
    
    if d == 3:
        if n == 3:
            if k >= 2:
                print("YES")
                print("1 2")
                print("2 3")
            else:
                print("NO")
        elif n == 4:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
            else:
                print("NO")
        elif n == 5:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
            else:
                print("NO")
        elif n == 6:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
            else:
                print("NO")
        elif n == 7:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
            else:
                print("NO")
        elif n == 8:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
            else:
                print("NO")
        elif n == 9:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
                print("8 9")
            else:
                print("NO")
        else:
            if k >= 4:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
                print("8 9")
                print("9 10")
            else:
                print("NO")
        sys.exit()
    
    if d == 4:
        if n == 4:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
            else:
                print("NO")
        elif n == 5:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
            else:
                print("NO")
        elif n == 6:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
            else:
                print("NO")
        elif n == 7:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
            else:
                print("NO")
        elif n == 8:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
            else:
                print("NO")
        elif n == 9:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
                print("8 9")
            else:
                print("NO")
        elif n == 10:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
                print("8 9")
                print("9 10")
            else:
                print("NO")
        else:
            if k >= 4:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
                print("8 9")
                print("9 10")
                print("10 11")
            else:
                print("NO")
        sys.exit()
    
    if d == 5:
        if n == 5:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
            else:
                print("NO")
        elif n == 6:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
            else:
                print("NO")
        elif n == 7:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
            else:
                print("NO")
        elif n == 8:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
            else:
                print("NO")
        elif n == 9:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
                print("8 9")
            else:
                print("NO")
        elif n == 10:
            if k >= 3:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
                print("8 9")
                print("9 10")
            else:
                print("NO")
        else:
            if k >= 4:
                print("YES")
                print("1 2")
                print("2 3")
                print("3 4")
                print("4 5")
                print("5 6")
                print("6 7")
                print("7 8")
                print("8 9")
                print("9 10")
                print("10 11")
            else:
                print("NO")
        sys.exit()
    
    print("YES")
    print("1 2")
    print("2 3")
    print("3 4")
    print("4 5")
    print("5 6")
    print("6 7")
    print("7 8")
    print("8 9")
    print("9 10")
    print("10 11")
    print("11 12")
    print("12 13")
    print("13 14")
    print("14 15")
    print("15 16")
    print("16 17")
    print("17 18")
    print("18 19")
    print("19 20")

main()