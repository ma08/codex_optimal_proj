

def main():
    #Get inputs
    x1, y1 = map(int, input().split()) #First point
    x2, y2 = map(int, input().split()) #Second point
    x3, y3 = map(int, input().split()) #Third point

    #Calculate the final X and Y values
    x4 = 0
    y4 = 0
    if x1 == x2: #If x1 is the same as x2, x4 is x3
        x4 = x3
    elif x1 == x3: #If x1 is the same as x3, x4 is x2
        x4 = x2
    else: #Otherwise, x4 is x1
        x4 = x1

    if y1 == y2: #If y1 is the same as y2, y4 is y3
        y4 = y3
    elif y1 == y3: #If y1 is the same as y3, y4 is y2
        y4 = y2
    else: #Otherwise, y4 is y1
        y4 = y1

    #Print the final X and Y values
    print(x4, y4)

if __name__ == "__main__":
    main()
