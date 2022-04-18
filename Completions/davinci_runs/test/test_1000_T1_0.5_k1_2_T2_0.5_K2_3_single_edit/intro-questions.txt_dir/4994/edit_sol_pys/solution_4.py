

def main():
    #Get inputs
    x1, y1 = map(int, input().split()) #First point
    x2, y2 = map(int, input().split()) #Second point
    x3, y3 = map(int, input().split()) #Third point

    #Calculate the final X and Y values
    x4 = 0 #Final X value
    y4 = 0 #Final Y value

    if x1 == x2:
        x4 = x3 #If the first X value is equal to the third X value, then the final X value is the second X value
    elif x1 == x3:
        x4 = x2 #If the first X value is equal to the second X value, then the final X value is the third X value
    else:
        x4 = x1 #If the second X value is equal to the third X value, then the final X value is the first X value

    if y1 == y2:
        y4 = y3 #If the first Y value is equal to the second Y value, then the final Y value is the third Y value
    elif y1 == y3:
        y4 = y2 #If the first Y value is equal to the third Y value, then the final Y value is the second Y value
    else:
        y4 = y1 #If the second Y value is equal to the third Y value, then the final Y value is the first Y value

    #Print the final X and Y values
    print(x4, y4)

if __name__ == "__main__":
    main()
