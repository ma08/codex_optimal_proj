
n = int(input())
c = [int(x) for x in input().split()]
c.sort()

# If the helium is too small, it is impossible to fill the balloons
if c[0] == 0:
    print("impossible")

# If the helium is large enough, we can fill the balloons from smallest to largest
else:
    # Find the minimum amount of helium needed to fill all balloons from smallest to largest
    min_helium_small = 0
    for i in range(1, n):
        min_helium_small += i

    # If there is too much helium, fill the balloons from smallest to largest
    if min_helium_small <= c[-1]:
        print(1)

    # If there is just enough helium to fill all balloons from smallest to largest, fill the balloons from largest to smallest
    elif min_helium_small == sum(c):
        print(1 / n + 1)

    # If there is not enough helium, fill the balloons from largest to smallest
    else:
        helium_used = 0
        for i in range(n - 1, 0, -1):
            helium_used += c[i - 1]
            if helium_used >= min_helium_small:
                print(helium_used / (n * i))
                break
