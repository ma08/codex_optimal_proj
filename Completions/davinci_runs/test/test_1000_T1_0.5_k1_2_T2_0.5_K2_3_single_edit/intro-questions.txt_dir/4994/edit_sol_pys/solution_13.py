

def main():
    #Get inputs
    x1, y1 = map(int, input().split()) # Get the coordinates of the first point
    x2, y2 = map(int, input().split()) # Get the coordinates of the second point
    x3, y3 = map(int, input().split()) # Get the coordinates of the third point

    #Calculate the final X and Y values
    x4 = 0
    y4 = 0
    if x1 == x2: # If the x values of the first and second point are equal
        x4 = x3
    elif x1 == x3: # If the x values of the first and third point are equal
        x4 = x2
    else: # If the x values of the second and third point are equal
        x4 = x1

    if y1 == y2: # If the y values of the first and second point are equal
        y4 = y3
    elif y1 == y3: # If the y values of the first and third point are equal
        y4 = y2
    else: # If the y values of the second and third point are equal
        y4 = y1

    #Print the final X and Y values
    print(x4, y4)

if __name__ == "__main__":
    main()
