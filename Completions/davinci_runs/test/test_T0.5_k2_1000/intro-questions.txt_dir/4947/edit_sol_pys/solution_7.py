

def main(): 
    x = float(input("Enter the distance in miles: "))
    print("The distance in kilometers is " + str(int(round(1000 * (5280/4854) * x))))

main()
