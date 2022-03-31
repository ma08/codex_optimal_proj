

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
        if a[i%3] > 0 and b[i%3] > 0: # if both a and b are greater than 0, then compare
            if i%3 == 0:
                if a[0] > b[0]:
                    a[0] -= 1
                    maximum += 1
                else:
                    b[0] -= 1
            elif i%3 == 1:
                if a[1] > b[1]:
                    a[1] -= 1
                    maximum += 1
                else:
                    b[1] -= 1
            else:
                if a[2] > b[2]:
                    a[2] -= 1
                    maximum += 1
                else:
                    b[2] -= 1
        elif a[i%3] > 0: # if a is greater than 0, then take it
            a[i%3] -= 1
            maximum += 1
        elif b[i%3] > 0: # if b is greater than 0, then take it
            b[i%3] -= 1
    for i in range(n):
        if a[i%3] > 0 and b[i%3] > 0: # if both a and b are greater than 0, then compare
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
        elif a[i%3] > 0: # if a is greater than 0, then take it
            a[i%3] -= 1
            minimum += 1
        elif b[i%3] > 0: # if b is greater than 0, then take it
            b[i%3] -= 1
    print(minimum,maximum)

main()
