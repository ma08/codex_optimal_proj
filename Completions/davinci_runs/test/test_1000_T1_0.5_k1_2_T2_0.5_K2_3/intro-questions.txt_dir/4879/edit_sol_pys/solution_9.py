
import sys

def main():
    #Read the input
    a,b,c = input().split()

    #Determine if you should yield or not
    if((a == "North" and b == "West" and c == "South") or (a == "South" and b == "East" and c == "North") or (a == "East" and b == "North" and c == "West") or (a == "West" and b == "South" and c == "East")):
        print("Yes")
    elif((a == "North" and b == "East" and c == "West") or (a == "South" and b == "West" and c == "East") or (a == "East" and b == "South" and c == "North") or (a == "West" and b == "North" and c == "South")):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
