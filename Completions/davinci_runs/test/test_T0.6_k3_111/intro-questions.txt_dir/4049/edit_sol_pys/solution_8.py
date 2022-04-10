

#-----Solution-----

#Main function
def main():
    #Get input and assign variables
    n = int(input())
    a1, a2, a3 = map(int, input().split())
    b1, b2, b3 = map(int, input().split())
    
    #Create and assign variables
    a_win = 0
    b_win = 0
    
    #Get the win count for A
    a_win += min(a1, b2)
    a1 -= min(a1, b2)
    b1 -= min(a1, b2)

    a_win += min(a2, b3)
    a2 -= min(a2, b3)
    b2 -= min(a2, b3)

    a_win += min(a3, b1)
    a1 -= min(a3, b1)
    b1 -= min(a3, b1)
    
    #Get the win count for B
    b_win += min(b1, a2)
    a2 -= min(b1, a2)
    b1 -= min(b1, a2)

    b_win += min(b2, a3)
    a3 -= min(b2, a3)
    b2 -= min(b2, a3)

    b_win += min(b3, a1)
    a1 -= min(b3, a1)
    b3 -= min(b3, a1)
    
    #Print the win count for each
    print(a_win, n-b_win)

main()
