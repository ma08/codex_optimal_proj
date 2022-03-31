
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

def color(n, k, a):
    if k == 1:
        print("YES")
        for i in range(n):
            print(1, end=" ")
        print("")
        return

    if k == 2:
        if n % 2 == 0:
            print("YES")
            for i in range(n):
                if i % 2 == 0:
                    print(1, end=" ")
                else:
                    print(2, end=" ")
            print("")
            return
        else:
            print("NO")
            return

    if k == 3:
        if n % 3 == 0:
            print("YES")
            for i in range(n):
                if i % 3 == 0:
                    print(1, end=" ")
                elif i % 3 == 1:
                    print(2, end=" ")
                else:
                    print(3, end=" ")
            print("")
            return
        else:
            print("NO")
            return

    if k == 4:
        if n % 4 == 0:
            print("YES")
            for i in range(n):
                if i % 4 == 0:
                    print(1, end=" ")
                elif i % 4 == 1:
                    print(2, end=" ")
                elif i % 4 == 2:
                    print(3, end=" ")
                else:
                    print(4, end=" ")
            print("")
            return
        else:
            print("NO")
            return

    if k == 5:
        if n % 5 == 0:
            print("YES")
            for i in range(n):
                if i % 5 == 0:
                    print(1, end=" ")
                elif i % 5 == 1:
                    print(2, end=" ")
                elif i % 5 == 2:
                    print(3, end=" ")
                elif i % 5 == 3:
                    print(4, end=" ")
                else:
                    print(5, end=" ")
            print("")
            return
        else:
            print("NO")
            return

    if k == 6:
        if n % 6 == 0:
            print("YES")
            for i in range(n):
                if i % 6 == 0:
                    print(1, end=" ")
                elif i % 6 == 1:
                    print(2, end=" ")
                elif i % 6 == 2:
                    print(3, end=" ")
                elif i % 6 == 3:
                    print(4, end=" ")
                elif i % 6 == 4:
                    print(5, end=" ")
                else:
                    print(6, end=" ")
            print("")
            return
        else:
            print("NO")
            return

color(n, k, a)
