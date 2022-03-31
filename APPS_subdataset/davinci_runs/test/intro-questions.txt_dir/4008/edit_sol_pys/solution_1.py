
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

def color(n, k, a):
    if n % k == 0:
        print("YES") 
        for i in range(n): 
            if i % k == 0:
                print(1, end=" ")
            elif i % k == 1:
                print(2, end=" ")
            elif i % k == 2:
                print(3, end=" ")
            elif i % k == 3:
                print(4, end=" ")
            elif i % k == 4:
                print(5, end=" ")
            else:
                print(6, end=" ")
        print() 
        return 

    print("NO")
    return

color(n, k, a)
