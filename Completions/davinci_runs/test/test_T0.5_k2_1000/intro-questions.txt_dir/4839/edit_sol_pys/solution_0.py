

n = int(input())
c = [int(x) for x in input().split()]
c.sort()

# If the helium is too small, it is impossible to fill the balloons.
if c[0] == 0:
    print("impossible") 

# If the helium is large enough, we can fill the balloons from smallest to largest.
else:
    # Find the minimum amount of helium needed to fill all balloons
    min_helium = 0
    for i in range(1, n + 1):
        min_helium += i

    # If there is too much helium, fill the balloons from smallest to largest
    if min_helium <= c[-1]:
        print(1) 

    # If there is just enough helium, fill the balloons from largest to smallest
    elif min_helium == sum(c):
        print(1 / n) 

    # If there is not enough helium, fill the balloons from largest to smallest
    else:
        helium_used = 0
        for i in range(n, 0, -1):
            helium_used += c[i - 1]
            if helium_used >= min_helium:
                print(helium_used / (n * i)) 
                break
