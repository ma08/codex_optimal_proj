
#----Solution----#

def main():
    n, m = map(int, input().split()) #inputs the number of rows and columns
    l = [] #creates a list
    count = 0 #initializes count
    for i in range(n): #iterates through the rows
        l.append(input()) #appends the input to the list
    for i in range(m): #iterates through the columns
        if l[0][i] == '_': #checks if the first row's column is a '_'
            count += 1 #increments count
    print(count) #prints count

main()
