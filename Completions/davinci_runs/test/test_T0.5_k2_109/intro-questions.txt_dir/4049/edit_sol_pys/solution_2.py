

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    a.reverse()
    b.reverse()
    minimum = 0
    maximum = 0
    for i in range(n):
        if a[i%3] > 0 and b[i%3] > 0: # check if both are greater than 0 
            if i%3 == 0:
                if a[0] > b[0]:
                    a[0] -= 1
                    maximum += 1 # if a[0] is greater than b[0] then a[0] will be decreased by 1 and maximum will be increased by 1
                else:
                    b[0] -= 1 # if a[0] is less than b[0] then b[0] will be decreased by 1
            elif i%3 == 1:
                if a[1] > b[1]:
                    a[1] -= 1
                    maximum += 1 # if a[1] is greater than b[1] then a[1] will be decreased by 1 and maximum will be increased by 1
                else:
                    b[1] -= 1 # if a[1] is less than b[1] then b[1] will be decreased by 1
            else:
                if a[2] > b[2]:
                    a[2] -= 1
                    maximum += 1 # if a[2] is greater than b[2] then a[2] will be decreased by 1 and maximum will be increased by 1
                else:
                    b[2] -= 1 # if a[2] is less than b[2] then b[2] will be decreased by 1
        elif a[i%3] > 0: # if a[i%3] is greater than 0
            a[i%3] -= 1
            maximum += 1
        elif b[i%3] > 0:
            b[i%3] -= 1
    for i in range(n):
        if a[i%3] > 0 and b[i%3] > 0:
            if i%3 == 0:
                if a[0] < b[0]:
                    a[0] -= 1
                    minimum += 1
                else:
                    b[0] -= 1
            elif i%3 == 1:
                if a[1] < b[1]:
                    a[1] -= 1
                    minimum += 1
                else:
                    b[1] -= 1
            else:
                if a[2] < b[2]:
                    a[2] -= 1
                    minimum += 1
                else:
                    b[2] -= 1
        elif a[i%3] > 0:
            a[i%3] -= 1
            minimum += 1
        elif b[i%3] > 0:
            b[i%3] -= 1
    print(minimum,maximum)

main()
